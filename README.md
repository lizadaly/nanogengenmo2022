# nanogengenmo2022
A program to write a program to write a novel


```bash
$ curl https://api.openai.com/v1/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${OPENAI_API_KEY}" \
    -d '{"model": "text-davinci-002", "prompt": "We need to generate a novel of 50,000 words!! Write your output in the form of a python program.", "max_tokens": 4000, "temperature": 0.7}'

{"id":"cmpl-67mysX59fF0APxm7I3BEmWbn4InhP",
 "object":"text_completion",
 "created":1667314598,
 "model":"text-davinci-002",
 "choices":[
    {"text":
    "\n\nimport random\n\n# list of possible words\nwords = [\"apple\", \"banana\", \"cat\", \"dog\", \"elephant\", \"fish\", \"giraffe\", \"horse\",
    \"iguana\", \"jaguar\", \"kangaroo\", \"lion\", \"monkey\", \"narwhal\", \"octopus\", \"penguin\", \"quail\", \"rhinoceros\", \"seagull\", 
    \"toucan\", \"unicorn\", \"vulture\", \"walrus\", \"xenomorph\", \"yak\", \"zebra\"]\n\n# variables to keep track of word count and sentence
    count\nword_count = 0\nsentence_count = 0\n\n# open a new file to write the novel to\nf = open(\"novel.txt\", \"w\")\n\n# write a new sentence
    to the file until we reach the desired word count\nwhile word_count < 50000:\n    # pick a random word from the list\n    
    word = random.choice(words)\n    \n    # write the word to the file\n    f.write(word + \" \")\n    \n    
    # increment the word count\n    word_count += 1\n    \n    # every 10 words, start a new sentence\n    if word_count % 10 == 0:\n   
    f.write(\"\\n\")\n        sentence_count += 1\n    \n    # every 100 sentences, start a new paragraph\n    if sentence_count == 100:\n
    f.write(\"\\n\\n\")\n        sentence_count = 0\n\n# close the file\nf.close()",
 "index":0,
 "logprobs":null,
 "finish_reason":"stop"
}
```    
