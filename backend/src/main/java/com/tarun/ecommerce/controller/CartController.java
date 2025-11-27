package com.tarun.ecommerce.controller;

import com.tarun.ecommerce.model.CartItem;
import com.tarun.ecommerce.service.CartService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/cart")
@CrossOrigin(origins = "*")
public class CartController {
    
    @Autowired
    private CartService cartService;
    
    @PostMapping
    public ResponseEntity<CartItem> addToCart(
            @RequestBody Map<String, Object> request,
            Authentication authentication) {
        String userId = authentication.getName();
        String productId = (String) request.get("productId");
        Integer quantity = ((Number) request.get("quantity")).intValue();
        
        try {
            CartItem item = cartService.addToCart(userId, productId, quantity);
            return ResponseEntity.ok(item);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().build();
        }
    }
    
    @GetMapping
    public ResponseEntity<List<CartItem>> getCart(Authentication authentication) {
        String userId = authentication.getName();
        List<CartItem> cart = cartService.getCart(userId);
        return ResponseEntity.ok(cart);
    }
    
    @GetMapping("/total")
    public ResponseEntity<Map<String, BigDecimal>> getCartTotal(Authentication authentication) {
        String userId = authentication.getName();
        BigDecimal total = cartService.getCartTotal(userId);
        Map<String, BigDecimal> response = new HashMap<>();
        response.put("total", total);
        return ResponseEntity.ok(response);
    }
    
    @DeleteMapping("/{productId}")
    public ResponseEntity<Void> removeFromCart(
            @PathVariable String productId,
            Authentication authentication) {
        String userId = authentication.getName();
        cartService.removeFromCart(userId, productId);
        return ResponseEntity.ok().build();
    }
    
    @DeleteMapping
    public ResponseEntity<Void> clearCart(Authentication authentication) {
        String userId = authentication.getName();
        cartService.clearCart(userId);
        return ResponseEntity.ok().build();
    }
}


