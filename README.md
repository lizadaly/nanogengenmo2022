# nanogengenmo2022
A program to write a program to write a novel

curl https://api.openai.com/v1/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${OPENAI_API_KEY}" \
    -d '{"model": "text-davinci-002", "prompt": "We need to generate a novel of 50,000 words!! Write your output in the form of a python program.", "max_tokens": 4000, "temperature": 0.7}'
    
