from os import listdir
from os.path import isfile, join
import json
import unicodedata as ud

# For the instagram posts that are downloaded and are in English (or you translated into English),
# this script processes their text, identifies the utf-16 emojis, replaces them with unicode emoji codes,
# and then removes them from the text. For instance, the script gets '\ud83d\udc46Like' and transforms it into '\U0001f446Like',
# where '\U0001f446' is the code for 👆 (backhand index pointing up) in https://unicode.org/emoji/charts/full-emoji-list.html.
# It then removes '\U0001f446' and keeps the rest of the text.
# When posts contain emojis that consist of one code (like the above) and not a combination of codes, then `get_emoji_meaning`
# can be used to identify the meaning of the emoji and potentially replace it in the text to enrich the meaning of the post.
# This script also identifies and tokenizes the hashtags in the post.


def get_text_with_unicode_emojis(text):
  """
  Get text with utf-16 encoded emojis and return 1) text with unicode emojis that could be replaced with their meaning
  2) text with unicode emojis that can be displayed as icons.
  """
  unicode_text = (text
  .decode("raw_unicode_escape")
  .encode('utf-16', 'surrogatepass')
  .decode('utf-16')
  .encode("raw_unicode_escape")
  .decode("latin_1")
  )  # \U0001f446Like
  text_to_print = (text
    .decode("raw_unicode_escape")
    .encode('utf-16', 'surrogatepass')
    .decode('utf-16')
  )   # 👆Like # \ud83d\udc46Like
  return unicode_text, text_to_print

def get_emoji_meaning(emoji_code):
  return ud.name(emoji_code)  # 👆 - backhand index pointing up

def get_text_without_emojis(text):
  # return (''.join([i if ord(i) < 128 else ' ' for i in text]))
  return text.encode('ascii', 'ignore').decode('utf-8')


onlyfiles = [f for f in listdir('translated_data') if isfile(join('translated_data', f))]

user_clean_text = {}
for file in onlyfiles:
    print(f'file: {file}')
    with open(f'translated_data/{file}', 'r', encoding='ascii') as f:
      post = json.load(fp=f)
      for user in post:
        # remove emojis
        unicode_text, text_to_print = get_text_with_unicode_emojis(post[user].encode('unicode-escape'))
        clean_text = get_text_without_emojis(text_to_print) 
        clean_text = clean_text.replace('\\n', ' ')
        # extract hashtags
        hashtags = ([i[1:]  for i in clean_text.split() if i.startswith("#") ])
        new_hashtags = [] # get combinations of hashtags
        if any('#' in i for i in hashtags):
          for hashtag in hashtags:
            if '#' in hashtag:
              new_hashtags = new_hashtags + hashtag.split('#')
        if new_hashtags:
          hashtags = hashtags + new_hashtags
          hashtags = [hashtag for hashtag in hashtags if not '#' in hashtag]  # remove the long combined hashtags and keep the tokenized ones
        clean_text = ' '.join(([i  for i in clean_text.split() if not i.startswith("#") ])) + ' ' + ' '.join(hashtags)
        # remove empty posts
        if clean_text and not clean_text.isspace():
          # print(f'post: {post[user]}')
          # print(f'hashtags: {hashtags}')
          # print(f'clean_text: {clean_text}')
          user_clean_text[user] = clean_text
      # write user text pairs in json file
      with open(f'clean_data/{file[:-5]}_clean.json', 'w', encoding='ascii') as f:
          json.dump(user_clean_text, f)
