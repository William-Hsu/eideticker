#!/bin/bash

INPUT_FILE=$1
OUTPUT_FILE=$2

# Create archive
TEMPDIR=`mktemp -d`
mkdir $TEMPDIR/images
FFMPEG="ffmpeg -vcodec rawvideo -f rawvideo -pix_fmt uyvy422 -r 60 -s hd1080 -i $INPUT_FILE --"
$FFMPEG $TEMPDIR/movie.avi
$FFMPEG $TEMPDIR/images/%d.png

# Get a temporary name for the archive (so we can copy to final location)
TEMPFILE=`tempfile --suffix .zip`
rm $TEMPFILE

# Copy over file, remove temporaries
pushd $TEMPDIR
zip -r $TEMPFILE ./*
popd
mv $TEMPFILE $OUTPUT_FILE
rm -rf $TEMPDIR $TEMPFILE
