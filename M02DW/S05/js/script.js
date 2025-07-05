var listDevices = [ "android", "iphone", "bb10", "ipad", "tablet" ];
var description = navigator.userAgent.toLowerCase();


// for( var i = 0; i < listDevices.length; i ++ ) {
//     currentDevice = checkDevice();
//     console.log( currentDevice );
//     if( currentDevice == "tablet" ) {
//         location.href = "http://localhost:3000/tablet.html";
//     }
//     else if( currentDevice == "phone" ) {
//         location.href = "http://localhost:3000/phone.html";
//     }
// }

function checkDevice( device ) {
    var currentDevice = "";
    switch( device ) {
        case "ipad":
            currentDevice = "tablet";
            break;
        case "iphone":
        case "bb10":
            currentDevice = "phone";
            break;
    }
    return currentDevice;
}
console.log( checkDevice( "ipad" ) );
console.log( checkDevice( "iphone" ) );
console.log( checkDevice( "bb10" ) );
