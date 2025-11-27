package com.tarun.ecommerce.service;

import com.tarun.ecommerce.model.Product;
import com.tarun.ecommerce.model.User;
import com.tarun.ecommerce.repository.ProductRepository;
import com.tarun.ecommerce.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.stream.Collectors;

@Service
public class RecommendationService {
    
    @Autowired
    private ProductRepository productRepository;
    
    @Autowired
    private UserRepository userRepository;
    
    public List<Product> getRecommendationsByProduct(String productId, int limit) {
        Product product = productRepository.findById(productId)
            .orElseThrow(() -> new RuntimeException("Product not found"));
        
        List<String> productCategories = product.getCategories();
        
        // Find products with similar categories
        List<Product> allProducts = productRepository.findAll();
        
        Map<Product, Double> similarityScores = new HashMap<>();
        
        for (Product p : allProducts) {
            if (p.getId().equals(productId)) {
                continue; // Skip the same product
            }
            
            // Calculate category similarity (Jaccard similarity)
            Set<String> productCats = new HashSet<>(productCategories);
            Set<String> pCats = new HashSet<>(p.getCategories());
            
            Set<String> intersection = new HashSet<>(productCats);
            intersection.retainAll(pCats);
            
            Set<String> union = new HashSet<>(productCats);
            union.addAll(pCats);
            
            double similarity = union.isEmpty() ? 0.0 : (double) intersection.size() / union.size();
            similarityScores.put(p, similarity);
        }
        
        // Sort by similarity and return top N
        return similarityScores.entrySet().stream()
            .sorted(Map.Entry.<Product, Double>comparingByValue().reversed())
            .limit(limit)
            .map(Map.Entry::getKey)
            .collect(Collectors.toList());
    }
    
    public List<Product> getRecommendationsByUser(String userId, int limit) {
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new RuntimeException("User not found"));
        
        List<String> userPreferences = user.getPreferences();
        
        if (userPreferences.isEmpty()) {
            // If no preferences, return popular products
            return productRepository.findAll().stream()
                .sorted((a, b) -> Integer.compare(b.getStock(), a.getStock())) // Sort by stock (popularity proxy)
                .limit(limit)
                .collect(Collectors.toList());
        }
        
        // Find products matching user preferences
        List<Product> allProducts = productRepository.findAll();
        
        Map<Product, Integer> matchScores = new HashMap<>();
        
        for (Product product : allProducts) {
            int matches = 0;
            for (String category : product.getCategories()) {
                if (userPreferences.contains(category)) {
                    matches++;
                }
            }
            matchScores.put(product, matches);
        }
        
        // Sort by match score and return top N
        return matchScores.entrySet().stream()
            .sorted(Map.Entry.<Product, Integer>comparingByValue().reversed())
            .limit(limit)
            .map(Map.Entry::getKey)
            .collect(Collectors.toList());
    }
}


