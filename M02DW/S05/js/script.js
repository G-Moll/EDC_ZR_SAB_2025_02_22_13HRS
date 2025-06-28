var listDevices = [ "android", "iphone", "BB10", "ipad", "tablet" ];
var description = navigator.userAgent.toLowerCase();

location.href = "http://localhost:3000/phone.html";

/*
for( var i = 0; i < listDevices.length; i ++ ) {
    // console.log( description.indexOf( listDevices[ i ] ) );
    if(
        description.indexOf( listDevices[ i ]  )
    ) {
        location.href = ""
    }
    else if( true ) {
    }
    console.log( listDevices[ i ] );
}

console.log( description );
*/
