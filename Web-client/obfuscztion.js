
function dechiffre(pass_enc){
    var pass = "70,65,85,88,32,80,65,83,83,87,79,82,68,32,72,65,72,65";
    var monpass  = pass_enc.split(',');
    var fauxpass = pass.split(',');
    convertAsciiToChar(fauxpass)
    var i,len_fauxpass,k,l=0,m,n,o,p = "";i = 0;
    len_fauxpass = fauxpass.length;
    k = len_fauxpass + (l) + (n=0);
    n = monpass.length;
    for(i = (o=0); i < (k = len_fauxpass = n); i++ ){
        o = monpass[i-l];p += String.fromCharCode((o = monpass[i]));
        if(i == 5)
        break;
    }

    for(i = (o=0); i < (k = len_fauxpass = n); i++ ){
        o = monpass[i-l]; 
        if(i > 5 && i < k-1)
            p += String.fromCharCode((o = monpass[i]));
    }

    p += String.fromCharCode(monpass[17]);
    pass = p;
    return pass;
}

function convertAsciiToChar() {
    let word = '';
    asciiList.forEach(asciiCode => {
        word += String.fromCharCode(asciiCode);
    });
    console.log(word);
}

console.log(dechiffre("\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30"));
/* 786OsErtk12 */