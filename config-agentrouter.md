Configure Environment VariablesNever hardcode your API key into your source files. Instead, save them as environment variables.For Linux/macOS (Terminal):bashexport OPENAI_API_KEY="your_agent_router_api_key_here"
export OPENAI_BASE_URL="https://agentrouter.org/v1"
Use code with caution.For Windows (PowerShell):powershell$env:OPENAI_API_KEY="your_agent_router_api_key_here"
$env:OPENAI_BASE_URL="https://agentrouter.org/v1"
Use code with caution.3. Code Integration ExamplesPython ImplementationIf you are using the official openai Python package, configure the client to point to AgentRouter's infrastructure.pythonfrom openai import OpenAI
import os

# Initialize client using AgentRouter credentials from environment variables
client = OpenAI(
    base_url=os.environ.get("OPENAI_BASE_URL", "https://agentrouter.org/v1"),
    api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-5",  # Replace with your desired target model slug
    messages=[{"role": "user", "content": "Hello, how are you?"}]
)

print(response.choices[0].message.content)
Use code with caution.Node.js / JavaScript Implementationjavascriptimport OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: process.env.OPENAI_BASE_URL || 'https://agentrouter.org/v1',
  apiKey: process.env.OPENAI_API_KEY,
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: 'gpt-5', // Replace with your desired target model slug
    messages: [{ role: 'user', content: 'Hello!' }],
  });

  console.log(completion.choices[0].message.content);
}

main();
Use code with caution.4. Configuration Requirements ReferenceWhen setting up AgentRouter inside existing AI IDE extensions (like Roo Code) or CLI frameworks (like Claude Code), always use these exact parameters:Provider Type: OpenAI CompatibleBase URL: https://agentrouter.org/v1API Key: Your generated token (sk-...)Authentication Scheme: Bearer Token