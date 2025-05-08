def get_opt_125m_layer_dimensions():  
    """  
    Returns a dictionary of matrix multiplication dimensions for OPT-125m model.  
    Each entry represents a specific operation in the transformer architecture.  
    """  
    hidden_size = 768  
    num_heads = 12  
    head_dim = hidden_size // num_heads  # 64  
    ffn_dim = hidden_size * 4  # 3072  
      
    layers = {}  
      
    # QKV projections (combined in one operation in OPT)  
    layers["qkv_projection"] = {  
        "M": hidden_size,
        "K": hidden_size,
        "N": 3 * hidden_size, 
        "density": 0.5,
        "distribution": "fixed_structured"  
    }  
      
    # Output projection after self-attention  
    layers["output_projection"] = {  
        "M": hidden_size,
        "K": hidden_size, 
        "N": hidden_size, 
        "density": 0.5,  
        "distribution": "fixed_structured"  
    }  
      
    # FFN first layer (expansion)  
    layers["ffn_first"] = {  
        "M": hidden_size,
        "K": ffn_dim, 
        "N": hidden_size, 
        "density": 0.5,  
        "distribution": "fixed_structured"  
    }  
      
    # FFN second layer (contraction)  
    layers["ffn_second"] = {  
        "M": ffn_dim, 
        "K": hidden_size,
        "N": hidden_size,
        "density": 0.5,  
        "distribution": "fixed_structured"  
    }  
      
    return layers