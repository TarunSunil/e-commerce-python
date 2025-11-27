package com.tarun.ecommerce.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.index.Indexed;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Document(collection = "products")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Product {
    @Id
    private String id;
    
    @Indexed
    private String name;
    
    private String description;
    
    @Indexed
    private List<String> categories = new ArrayList<>();
    
    private BigDecimal price;
    
    private List<String> images = new ArrayList<>();
    
    private Integer stock;
    
    private Map<String, String> attributes = new HashMap<>();
    
    public Product(String name, String description, List<String> categories, 
                   BigDecimal price, Integer stock) {
        this.name = name;
        this.description = description;
        this.categories = categories != null ? categories : new ArrayList<>();
        this.price = price;
        this.stock = stock;
        this.images = new ArrayList<>();
        this.attributes = new HashMap<>();
    }
}


