package com.tarun.ecommerce.service;

import com.tarun.ecommerce.dto.AuthResponse;
import com.tarun.ecommerce.dto.LoginRequest;
import com.tarun.ecommerce.dto.RegisterRequest;
import com.tarun.ecommerce.model.User;
import com.tarun.ecommerce.repository.UserRepository;
import com.tarun.ecommerce.security.JwtUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class AuthService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private PasswordEncoder passwordEncoder;
    
    @Autowired
    private JwtUtil jwtUtil;
    
    public AuthResponse register(RegisterRequest request) {
        if (userRepository.existsByEmail(request.getEmail())) {
            throw new RuntimeException("Email already exists");
        }
        
        User user = new User(
            request.getName(),
            request.getEmail(),
            passwordEncoder.encode(request.getPassword())
        );
        
        user = userRepository.save(user);
        
        String token = jwtUtil.generateToken(user.getEmail(), user.getId(), user.getRoles());
        
        return new AuthResponse(token, user.getId(), user.getEmail(), user.getName(), user.getRoles());
    }
    
    public AuthResponse login(LoginRequest request) {
        Optional<User> userOpt = userRepository.findByEmail(request.getEmail());
        
        if (userOpt.isEmpty() || !passwordEncoder.matches(request.getPassword(), userOpt.get().getPasswordHash())) {
            throw new RuntimeException("Invalid email or password");
        }
        
        User user = userOpt.get();
        String token = jwtUtil.generateToken(user.getEmail(), user.getId(), user.getRoles());
        
        return new AuthResponse(token, user.getId(), user.getEmail(), user.getName(), user.getRoles());
    }
}


