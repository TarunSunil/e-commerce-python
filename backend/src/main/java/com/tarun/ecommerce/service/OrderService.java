package com.tarun.ecommerce.service;

import com.tarun.ecommerce.model.CartItem;
import com.tarun.ecommerce.model.Order;
import com.tarun.ecommerce.model.Product;
import com.tarun.ecommerce.repository.CartItemRepository;
import com.tarun.ecommerce.repository.OrderRepository;
import com.tarun.ecommerce.repository.ProductRepository;
import com.tarun.ecommerce.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class OrderService {
    
    @Autowired
    private OrderRepository orderRepository;
    
    @Autowired
    private CartItemRepository cartItemRepository;
    
    @Autowired
    private ProductRepository productRepository;
    
    @Autowired
    private UserRepository userRepository;
    
    @Transactional
    public Order createOrder(String userId) {
        List<CartItem> cartItems = cartItemRepository.findByUserId(userId);
        
        if (cartItems.isEmpty()) {
            throw new RuntimeException("Cart is empty");
        }
        
        List<Order.OrderItem> orderItems = cartItems.stream()
            .map(item -> {
                Product product = productRepository.findById(item.getProductId())
                    .orElseThrow(() -> new RuntimeException("Product not found: " + item.getProductId()));
                
                if (product.getStock() < item.getQuantity()) {
                    throw new RuntimeException("Insufficient stock for product: " + product.getName());
                }
                
                // Update stock
                product.setStock(product.getStock() - item.getQuantity());
                productRepository.save(product);
                
                return new Order.OrderItem(item.getProductId(), item.getQuantity(), item.getPrice());
            })
            .collect(Collectors.toList());
        
        BigDecimal total = orderItems.stream()
            .map(item -> item.getPrice().multiply(BigDecimal.valueOf(item.getQty())))
            .reduce(BigDecimal.ZERO, BigDecimal::add);
        
        Order order = new Order(userId, orderItems, total);
        Order savedOrder = orderRepository.save(order);
        
        // Clear cart
        cartItemRepository.deleteByUserId(userId);
        
        // Update user's order list
        userRepository.findById(userId).ifPresent(user -> {
            user.getOrderIds().add(savedOrder.getId());
            userRepository.save(user);
        });
        
        return savedOrder;
    }
    
    public List<Order> getUserOrders(String userId) {
        return orderRepository.findByUserIdOrderByCreatedAtDesc(userId);
    }
    
    public Order getOrderById(String orderId) {
        return orderRepository.findById(orderId)
            .orElseThrow(() -> new RuntimeException("Order not found"));
    }
}


