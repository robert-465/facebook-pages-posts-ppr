thonimport json
import os

class Exporter:
    def __init__(self, posts):
        self.posts = posts
        self.output_dir = "output"

    def export_to_json(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        output_file = os.path.join(self.output_dir, "posts.json")
        with open(output_file, "w") as f:
            json.dump(self.posts, f, indent=4)

        print(f"Posts exported to {output_file}")