import sys

# Function to estimate cost of using the OpenAI TTS API based on character count
# It accepts the text as a command line argument.

def estimate_cost(text, cost_per_million_characters):
    num_characters = len(text)
    cost = (num_characters / 1_000_000) * cost_per_million_characters
    return num_characters, cost

# Main script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python estimate_cost.py <text>")
        sys.exit(1)

    input_text = " ".join(sys.argv[1:])
    cost_per_million_characters = 15.00  # $15.00 per 1 million characters (current price of TTS API)

    # Estimate cost
    num_characters, estimated_cost = estimate_cost(input_text, cost_per_million_characters)
    print(f"Estimated OpenAI Cost: ${estimated_cost:.4f}")
