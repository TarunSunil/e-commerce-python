package com.tarun.ecommerce.service;

import com.tarun.ecommerce.model.CartItem;
import com.tarun.ecommerce.model.Product;
import com.tarun.ecommerce.repository.CartItemRepository;
import com.tarun.ecommerce.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.List;
import java.util.Optional;

@Service
public class CartService {
    
    @Autowired
    private CartItemRepository cartItemRepository;
    
    @Autowired
    private ProductRepository productRepository;
    
    public CartItem addToCart(String userId, String productId, Integer quantity) {
        Product product = productRepository.findById(productId)
            .orElseThrow(() -> new RuntimeException("Product not found"));
        
        if (product.getStock() < quantity) {
            throw new RuntimeException("Insufficient stock");
        }
        
        Optional<CartItem> existingItem = cartItemRepository.findByUserIdAndProductId(userId, productId);
        
        if (existingItem.isPresent()) {
            CartItem item = existingItem.get();
            item.setQuantity(item.getQuantity() + quantity);
            return cartItemRepository.save(item);
        } else {
            CartItem newItem = new CartItem(userId, productId, quantity, product.getPrice());
            return cartItemRepository.save(newItem);
        }
    }
    
    public List<CartItem> getCart(String userId) {
        return cartItemRepository.findByUserId(userId);
    }
    
    public void removeFromCart(String userId, String productId) {
        cartItemRepository.deleteByUserIdAndProductId(userId, productId);
    }
    
    public void clearCart(String userId) {
        cartItemRepository.deleteByUserId(userId);
    }
    
    public BigDecimal getCartTotal(String userId) {
        List<CartItem> items = cartItemRepository.findByUserId(userId);
        return items.stream()
            .map(item -> item.getPrice().multiply(BigDecimal.valueOf(item.getQuantity())))
            .reduce(BigDecimal.ZERO, BigDecimal::add);
    }
}


