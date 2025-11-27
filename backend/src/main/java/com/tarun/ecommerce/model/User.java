package com.tarun.ecommerce.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.index.Indexed;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Document(collection = "users")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    @Id
    private String id;
    
    private String name;
    
    @Indexed(unique = true)
    private String email;
    
    private String passwordHash;
    
    private List<String> roles = new ArrayList<>();
    
    private List<String> preferences = new ArrayList<>();
    
    private List<String> orderIds = new ArrayList<>();
    
    private LocalDateTime createdAt;
    
    public User(String name, String email, String passwordHash) {
        this.name = name;
        this.email = email;
        this.passwordHash = passwordHash;
        this.roles = new ArrayList<>();
        this.roles.add("USER");
        this.preferences = new ArrayList<>();
        this.orderIds = new ArrayList<>();
        this.createdAt = LocalDateTime.now();
    }
}


