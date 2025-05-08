import os  
import yaml  
from opt_layers import get_opt_125m_layer_dimensions  
  
def generate_yaml_for_layer(layer_name, dimensions, output_dir):  
    """  
    Generate a YAML file for a specific layer using the provided dimensions.  
      
    Args:  
        layer_name: Name of the layer  
        dimensions: Dictionary containing M, K, N dimensions  
        output_dir: Directory where the YAML file will be saved  
    """  
    problem = {  
        "problem": {  
            "version": 0.4,  
            "instance": {  
                "K": dimensions["K"],  
                "M": dimensions["M"],  
                "N": dimensions["N"],  
                "densities": {  
                    "A": {  
                        "density": dimensions.get("density", 1.0),  
                        "distribution": dimensions.get("distribution", "fixed_structured")  
                    }  
                }  
            },  
            "shape": {  
                "name": "gemm_ABZ",  
                "dimensions": ["M", "N", "K"],  
                "data_spaces": [  
                    {  
                        "name": "A",  
                        "projection": [[["M"]], [["K"]]]  
                    },  
                    {  
                        "name": "B",  
                        "projection": [[["N"]], [["K"]]]  
                    },  
                    {  
                        "name": "Z",  
                        "projection": [[["M"]], [["N"]]],  
                        "read_write": True  
                    }  
                ]  
            }  
        }  
    }  
      
    os.makedirs(output_dir, exist_ok=True)  
      
    filename = f"M{dimensions['M']}-K{dimensions['K']}-N{dimensions['N']}.yaml"  
    file_path = os.path.join(output_dir, filename)  
      
    with open(file_path, 'w') as f:  
        yaml.dump(problem, f, default_flow_style=False)  
      
    print(f"Generated YAML file: {file_path}")  
  
def main():  
    output_dir = "/home/workspace/example_designs/layer_shapes/MM/OPT125m_repr"
      
    opt_layers = get_opt_125m_layer_dimensions()  
      
    for layer_name, dimensions in opt_layers.items():  
        generate_yaml_for_layer(layer_name, dimensions, output_dir)  
      
    print(f"All YAML files generated in {output_dir}")  
  
if __name__ == "__main__":  
    main()