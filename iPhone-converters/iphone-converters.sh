
function heic2jpeg {
    cd $1
    for i in *.heic; do 
        convert -quality 98 "$i" "${i%.heic}.jpg"
    done
    cd - 
}


function mov2mp4 {
    cd $1
    for i in *.mov; do 
        ffmpeg -i "$i" "${i%.mov}.mp4"
    done
    cd - 
}

