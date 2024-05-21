# Reflection

## Part 2

While the generated data was pretty accurate, there are inherint risks. While adding a seed can lead to more (but not fully!) deterministic results (https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter), we would still want a human to read over the content before publishing it.

Even in this rather innocuous example, chatGPT ended the social media post with "exciting news", which sounds a bit "clickbait-y". For serious or tragic events, the moral (and legal) consequences could be dire. It is hard to really safeguard with code against such an event, because it would require protecting against so many possible scenarios. So generating drafts seems wise, at least during a long and thorough implementation process.

Finally, we must always remember that this model understands the context only in sets of tokens: numbers it stores internally. It has no true "understanding", because internally it is made up of mathematical and statistical modelling, and not actually intelligence.



## Part 3

I used ChatGPT in the browser (https://chatgpt.com/share/67d7310a-64ee-48a8-8f99-cc8b6016885a) to generate the boilerplate code for processing the text files, the terminal app and calling the API.

It had trouble with the examples (I hard-coded 3 examples but with more time would obviously have made some sort of loop structure), and also polished the terminal interface a bit more.