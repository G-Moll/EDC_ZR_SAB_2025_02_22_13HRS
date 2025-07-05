var listDevices = [ "android", "iphone", "bb10", "ipad", "tablet" ];
var description = navigator.userAgent.toLowerCase();

for( var i = 0; i < listDevices.length; i ++ ) {
    if( description.indexOf( listDevices[ i ] ) >= 0 ) {
        currentDevice = checkDevice( listDevices[ i ] );
        if( currentDevice == "tablet" ) {
            location.href = "http://localhost:3000/tablet.html";
        }
        else if( currentDevice == "phone" ) {
            location.href = "http://localhost:3000/phone.html";
        }
        break;
    }
}

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
