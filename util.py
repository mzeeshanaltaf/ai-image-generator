model_diff = """
| **Feature**              | **Stable Diffusion 2.1**              | **Stable Diffusion 3.5 Large**       |
|---------------------------|---------------------------------------|--------------------------------------|
| **Image Quality**         | High                                 | Superior (more realistic & detailed)|
| **Prompt Understanding**  | Good                                 | Excellent                           |
| **Model Size**            | Smaller                              | Larger                              |
| **Performance**           | Faster, less resource-intensive      | Resource-intensive, higher quality  |
| **Use Case**              | Broad general-purpose applications   | Demanding, high-fidelity tasks      |
| **Computational Needs**   | Mid-range GPUs                       | High-end GPUs or cloud platforms    |
"""

pre_defined_prompts = [
    # Nature and Landscapes
    "A surreal forest where the trees have glowing neon leaves, under a galaxy-filled night sky.",
    "A crystal-clear underwater world with colorful coral reefs and a school of futuristic, robotic fish.",
    "A desert oasis with golden sand dunes, a shimmering blue lake, and a floating castle in the distance.",
    
    # Fantasy and Sci-Fi
    "A steampunk city with airships flying between towering mechanical skyscrapers.",
    "A majestic dragon perched on a glowing mountain, surrounded by floating islands in the sky.",
    "An astronaut discovering an alien planet with bioluminescent plants and double suns on the horizon.",
    
    # Architecture and Urban Scenes
    "A futuristic city where all buildings are shaped like geometric crystals, reflecting a vibrant sunset.",
    "A quaint cobblestone village with colorful houses, surrounded by blooming cherry blossom trees.",
    "A floating market above the clouds, with hot air balloons serving as shops.",
    
    # Abstract and Conceptual
    "A fusion of fire and water, creating a vibrant, swirling vortex of flames and waves.",
    "An abstract painting brought to life, with dripping rainbow paint forming a 3D sculpture.",
    "A clock melting over a desert landscape, inspired by surrealist art styles.",
    
    # Whimsical and Fun
    "A giant panda wearing a suit and tie, sipping tea in an elegant Victorian-style room.",
    "A spaceship shaped like a giant slice of pizza, zooming through a galaxy of soda planets.",
    "A tea party with animated teacups and desserts dancing on the table.",
    
    # Historical and Mythical
    "A Viking warrior sailing a glowing aurora-lit sea, with mythical sea creatures swimming below.",
    "A Greek goddess standing in a marble temple, surrounded by golden light and ethereal clouds.",
    "A samurai meditating under a waterfall, with cherry blossoms floating in the breeze.",
    
    # Cosmic and Futuristic
    "A cyberpunk city with glowing holograms, neon signs, and flying cars zipping through the air.",
    "A black hole consuming a distant star, with colorful cosmic energy spiraling around it.",
    "An AI-powered garden with glowing mechanical flowers and robotic bees pollinating them."
]
