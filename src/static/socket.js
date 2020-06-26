var socket = io('http://localhost:3000');
socket.on('connect', function(){
    alert('Successfully connected to the backend :)');
});

sendToServer = () => {
    let data = document.getElementById('myNumber').value;
    console.log('sending ' + data);
    socket.emit('number_recv', data);
}

