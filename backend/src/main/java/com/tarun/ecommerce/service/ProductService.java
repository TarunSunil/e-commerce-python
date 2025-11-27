package com.tarun.ecommerce.service;

import com.tarun.ecommerce.model.Product;
import com.tarun.ecommerce.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ProductService {
    
    @Autowired
    private ProductRepository productRepository;
    
    public List<Product> getAllProducts(int page, int size, String category, String search) {
        Pageable pageable = PageRequest.of(page, size);
        
        if (search != null && !search.isEmpty()) {
            return productRepository.searchProducts(search);
        }
        
        if (category != null && !category.isEmpty()) {
            return productRepository.findByCategoriesContaining(category);
        }
        
        return productRepository.findAll(pageable).getContent();
    }
    
    public Optional<Product> getProductById(String id) {
        return productRepository.findById(id);
    }
    
    public Product createProduct(Product product) {
        return productRepository.save(product);
    }
    
    public Product updateProduct(String id, Product product) {
        Product existing = productRepository.findById(id)
            .orElseThrow(() -> new RuntimeException("Product not found"));
        
        existing.setName(product.getName());
        existing.setDescription(product.getDescription());
        existing.setCategories(product.getCategories());
        existing.setPrice(product.getPrice());
        existing.setImages(product.getImages());
        existing.setStock(product.getStock());
        existing.setAttributes(product.getAttributes());
        
        return productRepository.save(existing);
    }
    
    public void deleteProduct(String id) {
        if (!productRepository.existsById(id)) {
            throw new RuntimeException("Product not found");
        }
        productRepository.deleteById(id);
    }
}


