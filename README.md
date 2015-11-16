# distorteddecade.com

The website for the band, check them out.

## Making Changes

If you need to make minor changes to the site's contents: adding/removing gigs, changing text on the home page, etc. etc. Then you can do that by editing the files here in GitHub.

For any larger changes, or for help on anything, just ask Billy.

### Changing the Home Page

There's a file listed above called `index.html`, if you click on it you'll see its current contents. If you then click the pencil "edit" icon you'll be able to change things around.

Ignore the top of the file where there are the `---` lines, the stuff below them is the content.

This is an HTML page so if you're happy with HTML, have a play around. When you're done, there's a box at the bottom of the page for "committing" your changes. Just describe what changes you've made and then click "Commit changes".

It might take a while for the changes to show up on the live site. Maybe up to an hour.

### Changing the Bio Page

This is very similar to changing the home page, the only difference is that the page is a Markdown page (instead of HTML). Markdown is a very simple text format that should mean you can just write your changes in normal text without having to add the HTML tags.

### Changing the Music Page

The music page is auto-generated using the information found in the `_data` folder. There's a file in there called `music.yml` you have to add and remove entries to this file when you want to change which embedded players you can see.

Each entry in the file has a name and an embed code. To add a new embedded player to the page simply add a new chunk to the file that looks like this:

    - name: NAME
      embed: EMBED

Changing `NAME` to be what ever you'd like to call it, and `EMBED` to the HTML code that the player's source (e.g. YouTube, Facebook, SoundCloud) would give you. Make sure you keep the hyphen in there, it's important.

To remove a player, just delete that block (including the hyphen).

### Changing the Gigs Page

This is similar to the music page in that it's auto-generated. This time the data is kept in `_data/gig.yml` and each entry should look like:

- name: NAME
  location: LOCATION
  date: DATE
  time: "TIME"
  blurb: BLURB
  website: WEBSITE

`TIME` needs to be in quotes, for a frustrating reason.

`WEBSITE` can be removed if there's no link to point to. If you add one then the `NAME` will also be a link.
