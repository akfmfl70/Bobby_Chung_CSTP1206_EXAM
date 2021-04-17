console.log('loaded script');

function hello() {
    const helloDiv = document.querySelector('#hello-data')

    console.log('data set is: ', helloDiv.dataset.hello)
    const data = JSON.parse(helloDiv.dataset.hello)
    console.log('the data is: ', data)

    let output = ''
    if (data.phoneNumber) {
        output += 'Phone Number: ' + data.phoneNumber
    }
    if (data.email) {
        if (data.phoneNumber) {
            output += '\n'
        }
        output += 'Email: ' + data.email
    }
    window.alert(output)
}
