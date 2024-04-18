//Sample code that allows for the extracting of external website/apis to be able to update the locations of the server.

//SAMPLE ONE OF READING the API
import { fetch } from 'wix-fetch'; // Import fetch API from Wix

// Function to fetch data from the Random User Generator API
function fetchDataFromAPI() {
    return fetch('https://randomuser.me/api/') // Random User Generator API endpoint
        .then(response => response.json());
}

// Function to extract the word "result" and add it as an option in the dropdown menu
function extractResultAndAddToDropdown(data) {
    const resultWord = "result"; // Assuming you want to extract the word "result"
    const dropdownOption = { label: resultWord, value: resultWord };

    // Assuming #dropdown1 is the ID of your dropdown element in Wix
    $w('#dropdown1').options = [dropdownOption];
}

// Function to handle errors
function handleError(error) {
    console.error('Error fetching data:', error);
}

// Call the function to fetch data from the API and add the option to the dropdown when the page loads
$w.onReady(function () {
    fetchDataFromAPI()
        .then(extractResultAndAddToDropdown)
        .catch(handleError);
});

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//From external webpage that allows cors => just getting the first word

import { fetch } from 'wix-fetch'; // Import fetch API from Wix

// Function to fetch HTML content from an external website using CORS Anywhere
function fetchHTMLContent() {
    const url = 'https://cors-anywhere.herokuapp.com/https://en.wikipedia.org/wiki/Main_Page';
    return fetch(url)
        .then(response => response.text());
}

// Function to extract the first word from the HTML content
function extractFirstWord(htmlContent) {
    const textContent = htmlContent.replace(/<[^>]*>/g, ''); // Remove HTML tags
    const words = textContent.split(/\s+/); // Split text into words

    // Get the first non-empty word from the text content
    const firstWord = words.find(word => word.trim() !== '');

    if (firstWord) {
        return firstWord; // Return the first word
    } else {
        throw new Error('No word found in HTML content');
    }
}

// Function to populate dropdown options in Wix
function populateDropdownOptions() {
    fetchHTMLContent()
        .then(htmlContent => {
            const firstWord = extractFirstWord(htmlContent); // Extract the first word from HTML content
            const dropdownOption = { label: firstWord, value: firstWord };

            // Assuming #dropdown1 is the ID of your dropdown element in Wix
            $w('#dropdown1').options = [dropdownOption];
        })
        .catch(error => {
            console.error('Error fetching HTML content:', error);
        });
}

// Call the function to populate dropdown options when the page loads
$w.onReady(function () {
    populateDropdownOptions();
});


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// This code will be sample for the location checking and order for the dropdown menu option.
//THIS CODE BELOW ONLY GETS THE CURRENT LOCATION OF THE USER AND PUTS IT IN THE DROPDOWN MENU OPTION

import wixWindow from 'wix-window';

$w.onReady(function () {
    // Fetch user's IP address using a third-party service
    fetch('https://api.ipify.org?format=json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const ipAddress = data.ip;

            // Use an IP geolocation service to get user's country based on IP address
            fetch(`https://api.ipgeolocation.io/ipgeo?apiKey=eaee339a338f4bab9aa85cdac2b43c6b&ip=${ipAddress}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    const userCountry = data.country_name;

                    // Add user's country as an option to the dropdown menu
                    $w('#dropdown1').options = [{
                        label: userCountry,
                        value: userCountry
                    }];
                })
                .catch(error => {
                    console.error('Error fetching user location:', error);
                });
        })
        .catch(error => {
            console.error('Error fetching user IP:', error);
        });
});
