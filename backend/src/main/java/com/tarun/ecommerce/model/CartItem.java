package com.tarun.ecommerce.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.index.Indexed;

import java.math.BigDecimal;

@Document(collection = "carts")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class CartItem {
    @Id
    private String id;
    
    @Indexed
    private String userId;
    
    private String productId;
    
    private Integer quantity;
    
    private BigDecimal price;
    
    public CartItem(String userId, String productId, Integer quantity, BigDecimal price) {
        this.userId = userId;
        this.productId = productId;
        this.quantity = quantity;
        this.price = price;
    }
}


