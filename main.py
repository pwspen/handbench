from core.gen_tables import generate_table_files
from core.bench import run_benchmark

prompt = "How many fingers are in this image, including thumbs? Respond with ONLY a worded number, like 'Five'."

models = [
    "openrouter/openai/gpt-5.2",
    "openrouter/google/gemini-3-pro-preview",
    "openrouter/anthropic/claude-opus-4.5",
    "openrouter/x-ai/grok-4-fast",
    "openrouter/qwen/qwen3-vl-235b-a22b-instruct"
# Could also test
    # "openrouter/z-ai/glm-4.6v",
    # "openrouter/nvidia/nemotron-3-nano-30b-a3b:free",
    # "openrouter/google/gemma-3-27b-it",
    # "openrouter/google/gemini-2.5-flash",
    # "openrouter/qwen/qwen3-vl-8b-instruct",
]

if run_benchmark( # Returns True on success
    prompt=prompt,
    models=models
): # Other args: system, images_dir, log_dir, temperature, max_tokens
    print("Benchmark completed successfully.")

    generate_table_files(
        do_accuracy=True,
        do_models=True,
        do_answers=True
    )
    # Requires paths for logs, images, and output folders - pass as args log_dir, images_dir, output_dir, defaults are "logs/", "images/", "tables/" respectively