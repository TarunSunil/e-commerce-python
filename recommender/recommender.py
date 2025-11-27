from typing import List, Dict
from collections import Counter

class ContentBasedRecommender:
    """
    Content-based recommendation system using category similarity.
    """
    
    def recommend_by_product(self, product: Dict, all_products: List[Dict], limit: int = 5) -> List[Dict]:
        """
        Recommend products similar to the given product based on category overlap.
        Uses Jaccard similarity on categories.
        """
        product_categories = set(product.get('categories', []))
        product_id = product.get('id')
        
        # Calculate similarity scores
        similarities = []
        for p in all_products:
            if p.get('id') == product_id:
                continue  # Skip the same product
            
            p_categories = set(p.get('categories', []))
            
            # Jaccard similarity
            intersection = len(product_categories & p_categories)
            union = len(product_categories | p_categories)
            
            similarity = intersection / union if union > 0 else 0.0
            
            similarities.append((similarity, p))
        
        # Sort by similarity (descending) and return top N
        similarities.sort(key=lambda x: x[0], reverse=True)
        recommendations = [p for _, p in similarities[:limit]]
        
        return recommendations
    
    def recommend_by_user_preferences(self, user_preferences: List[str], 
                                      all_products: List[Dict], limit: int = 5) -> List[Dict]:
        """
        Recommend products based on user preferences (categories they like).
        """
        if not user_preferences:
            # If no preferences, return popular products (by stock)
            return sorted(all_products, key=lambda x: x.get('stock', 0), reverse=True)[:limit]
        
        user_pref_set = set(user_preferences)
        
        # Score products by how many preferred categories they match
        scored_products = []
        for p in all_products:
            p_categories = set(p.get('categories', []))
            match_count = len(user_pref_set & p_categories)
            scored_products.append((match_count, p))
        
        # Sort by match count (descending) and return top N
        scored_products.sort(key=lambda x: x[0], reverse=True)
        recommendations = [p for _, p in scored_products[:limit]]
        
        return recommendations


