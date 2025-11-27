package com.tarun.ecommerce.controller;

import com.tarun.ecommerce.model.Product;
import com.tarun.ecommerce.service.RecommendationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/recommend")
@CrossOrigin(origins = "*")
public class RecommendationController {
    
    @Autowired
    private RecommendationService recommendationService;
    
    @GetMapping("/{productId}")
    public ResponseEntity<List<Product>> getRecommendationsByProduct(
            @PathVariable String productId,
            @RequestParam(defaultValue = "5") int limit) {
        try {
            List<Product> recommendations = recommendationService.getRecommendationsByProduct(productId, limit);
            return ResponseEntity.ok(recommendations);
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }
    
    @GetMapping("/user/{userId}")
    public ResponseEntity<List<Product>> getRecommendationsByUser(
            @PathVariable String userId,
            @RequestParam(defaultValue = "5") int limit,
            Authentication authentication) {
        String authenticatedUserId = authentication.getName();
        
        // Users can only get their own recommendations
        if (!authenticatedUserId.equals(userId)) {
            return ResponseEntity.status(org.springframework.http.HttpStatus.FORBIDDEN).build();
        }
        
        try {
            List<Product> recommendations = recommendationService.getRecommendationsByUser(userId, limit);
            return ResponseEntity.ok(recommendations);
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }
}


