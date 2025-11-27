package com.tarun.ecommerce.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.index.Indexed;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Document(collection = "orders")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Order {
    @Id
    private String id;
    
    @Indexed
    private String userId;
    
    private List<OrderItem> items = new ArrayList<>();
    
    private String status; // placed, confirmed, shipped, delivered, cancelled
    
    private BigDecimal total;
    
    private LocalDateTime createdAt;
    
    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class OrderItem {
        private String productId;
        private Integer qty;
        private BigDecimal price;
    }
    
    public Order(String userId, List<OrderItem> items, BigDecimal total) {
        this.userId = userId;
        this.items = items != null ? items : new ArrayList<>();
        this.status = "placed";
        this.total = total;
        this.createdAt = LocalDateTime.now();
    }
}


