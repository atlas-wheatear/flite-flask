# flite-flask

This will contain the code for the flite docker-container component of my
(SID 1800209) project for the module Cloud Computing at ARU.

## Limitations

- Requires a space in the text string of the json to return a file, single words are ignored

## Intended Purpose

This should **_not_** ever be made directly available to the public internet.
It is intended to generate TTS recordings, from strings provided by the game server
that are then sent to a _.ogg_ file server (potentially supported by a redis cache).

## A note on FFmpeg

FFmpeg is required for the purposes of header repair
because the _.ogg_ files genereated by flite are corrupt,
and can't be played in the godot engine.
