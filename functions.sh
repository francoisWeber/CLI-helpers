# pics
function heic2jpeg {
    for i in *.HEIC; do 
        convert -quality 100 "$i" "${i%.HEIC}.jpg"
    done
    for i in *.heic; do 
        convert -quality 100 "$i" -o "${i%.heic}.jpg"
    done
    jhead -ft *.jpg
}


function any2jpeg {
    # argument : extension you want to turn into JPG
    for i in *."$1"; do 
        convert -quality 98 -define "$1":exif-properties=true "$i" "${i%.$1}.jpg"
        rm "$i"
    done
}

function mov2mp4 {

    for i in *.MOV; do 
        ffmpeg -i "$i" "${i%.mov}.mp4"
        rm "$i"
    done 
    for i in *.mov; do 
        ffmpeg -i "$i" "${i%.mov}.mp4"
        rm "$i"
    done
}


# Add my tools to path
export PATH="$PATH:~/Code/CLI-helpers/pics-handling"