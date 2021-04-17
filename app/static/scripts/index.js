console.log('loaded script');

    
export function createUser() {

    const data = {
        name: 'Princess Peach',
        sex: 'female',
        bio: 'a super cool lady who loves plumbers, and sunsets, and tastey grass....',
        dName: 'PeachyPrincess',
        age: '24',
        hobbiesList: ['dancing', 'golfing', 'tennis', 'go karting', 'sun bathing'],
        contactList: {'email': 'peach@anEmail.com', 'phoneNumber': '(123)456-7890'}
    }

    fetch(
        "/create",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    ).then(
        (response) => {
            return response.json();
        }
    ).then(
        (json) => {
            console.log("successful post", json);
            const message = json.message
            window.alert(message)
        }
    ).catch(
        (error) => {
            console.error("error", error);
        }
    );
}

