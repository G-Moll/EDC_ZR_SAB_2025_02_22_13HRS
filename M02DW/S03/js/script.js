var content = document.getElementById("content" );
var endpoint = "https://jsonplaceholder.typicode.com/users";
var xhr = new XMLHttpRequest();
xhr.open( "GET", endpoint, true );
xhr.send();
xhr.addEventListener( "load", loadResponseData );

function loadResponseData( e ) {
    var responseData = JSON.parse( e.target.responseText );
    console.log( responseData[ 0 ].id );
    console.log( responseData[ 0 ].name );
    console.log( responseData[ 0 ].email );
}

content.innerHTML = "<h1>Hello DOM</h1>";

// console.log( endpoint );
// console.log( content );
