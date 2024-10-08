// script.js

document.addEventListener('DOMContentLoaded', function() {
    const locations = [' Devarabeesana Halli',
    ' Devarachikkanahalli',
    '1st Block BEL Layout',
    '1st Block HBR Layout',
    '1st Block HRBR Layout',
    '1st Block Jayanagar',
    '1st Block Koramangala',
    '1st Phase JP Nagar',
    '1st Stage Indira Nagar',
    '2nd Block Bel Layout',
    '2nd Block Hrbr Layout',
    '2nd Block Jayanagar',
    '2nd Phase JP Nagar',
    '2nd Phase Judicial Layout',
    '2nd Stage Arekere Mico Layout',
    '2nd Stage Nagarbhavi',
    '3rd Block Banashankari',
    '3rd Block Hrbr Layout',
    '3rd Block Jayanagar',
    '3rd Block Koramangala',
    '3rd Phase JP Nagar',
    '4th Block Jayanagar',
    '4th Block Koramangala',
    '4th Phase JP Nagar',
    '4th T block Jayanagar',
    '5th Block Hbr Layout',
    '5th Phase JP Nagar',
    '5th Stage BEML Layout',
    '6th Phase JP Nagar',
    '6th block Koramangala',
    '7th Block Jayanagar',
    '7th Phase JP Nagar',
    '8th Block Jayanagar',
    '8th Phase JP Nagar',
    '8th block Koramangala',
    '9th Block Jayanagar',
    '9th Phase JP Nagar',
    'A Narayanapura',
    'AECS Layout',
    'AGS Layout',
    'AMS Layout',
    'Abbaiah Reddy Layout',
    'Abbigere',
    'Aishwarya Crystal Layout',
    'Akshaya Nagar',
    'Akshaya Vana',
    'Akshayanagara East',
    'Akshayanagara West',
    'Akshya Nagar',
    'Alfa Garden Layout',
    'Amam Enclave Layout',
    'Amarjyothi Colony',
    'Ambalipura',
    'Ambedkar Colony',
    'Ambedkar Nagar',
    'Amblipura',
    'Amruthahalli',
    'Amruthnagar',
    'Anand Nagar',
    'Anand nagar',
    'Anandapura',
    'Anantapura',
    'Ananth Nagar',
    'Andrahalli',
    'Anekal',
    'Anjana Nagar',
    'Anjanapura',
    'Anjappa Layout',
    'Ankappa Layout',
    'Annapurneshwari Nagar',
    'Anugrah Layout',
    'Ardendale',
    'Arehalli',
    'Arekere',
    'Ashirvad Colony',
    'Ashwath Nagar',
    'Ashwathnagar',
    'Atmananda Colony',
    'Attibele',
    'Attur Layout',
    'Austin Town',
    'Avalahalli',
    'Ayappa Nagar',
    'B Channasandra',
    'B Narayanapura',
    'BCC Layout',
    'BCMC Layout',
    'BEL Road',
    'BEML Layout',
    'BHEL Layout',
    'BSM Extension',
    'BTM 1st Stage',
    'BTM 2nd Stage',
    'BTM 4th Stage',
    'BTM Layout',
    'Baba Nagar',
    'Babusapalaya',
    'Badavala Nagar',
    'Bagalakunte',
    'Bagalur',
    'Bagalur Main Road',
    'Balagere',
    'Banagiri Nagar',
    'Banashankari',
    'Banashankari Stage II',
    'Banashankari Stage III',
    'Banashankari Stage V',
    'Banashankari Stage VI',
    'Banaswadi',
    'Banjara Layout',
    'Bank Of Baroda Colony',
    'Bannerghatta',
    'Bannerghatta Road',
    'Basapura',
    'Basava Nagar',
    'Basavanagara',
    'Basavanapura',
    'Basavangudi',
    'Basavanna Nagar',
    'Basaveshwara Nagar',
    'Basaveshwara Nagar Yelahanka',
    'Battarahalli',
    'Begur',
    'Begur Road',
    'Belathur',
    'Belatur',
    'Bellandur',
    'Bellari Road',
    'Bendiganahalli',
    'Benson Town',
    'Bethel Nagar',
    'Bharathi Nagar',
    'Bhoganhalli',
    'Bhoopsandra',
    'Bhuvaneshwari Nagar',
    'Bhuvaneswari Nagar',
    'Bidadi',
    'Bikasipura',
    'Bileshivale',
    'Billekahalli',
    'Binny Pete',
    'Bisuvanahalli',
    'Bommanahalli',
    'Bommasandra',
    'Bommasandra Industrial Area',
    'Bommenahalli',
    'Brindavan Layout',
    'Brindavan Nagar',
    'Brooke Bond First Cross',
    'Brookefield',
    'Budigere',
    'Byadarahalli',
    'Byagadadhenahalli',
    'Byatarayanapura',
    'Byrasandra',
    'Byrathi Village',
    'CQAL Layout',
    'CV Raman Nagar',
    'Cambridge Layout',
    'Canara Bank Colony',
    'Canara Bank Layout',
    'Carmelaram',
    'Challaghatta',
    'Chamrajpet',
    'Chamundi Nagar',
    'Chandapura',
    'Chandra Layout',
    'Channasandra',
    'Channasandra Layout',
    'Chelekare',
    'Chennammana Kere',
    'Chennammanakere Achukattu',
    'Chennappa Layout',
    'Chikka Banaswadi',
    'Chikka Tirupathi',
    'Chikkabanavar',
    'Chikkadunnasandra',
    'Chikkakannalli',
    'Chikkalasandra',
    'Chikkasandra',
    'Chikkathoguru',
    'Chikku Lakshmaiah Layout',
    'Chinnapanahalli',
    'Cholanayakanahalli',
    'Choodasandra',
    'Classic Paradise Layout',
    'Cleveland Town',
    'Coconut Garden',
    'Coconut Grove Layout',
    'Coffee Board Layout',
    'Cooke Town',
    'Cottonpet',
    'Cox Town',
    'Crimson Layout',
    'Cunningham Road',
    'D Group Employees Layout',
    'Daadys Gaarden Layout',
    'Dairy Circle',
    'Dasanapura',
    'Dasappa Layout',
    'Dasarahalli',
    'Defence Colony',
    'Dena Bank Colony',
    'Devanahalli',
    'Devanahalli Int. Airport',
    'Devanahalli Road',
    'Devara Jeevanahalli',
    'Devasandra Extension',
    'Devasthanagalu',
    'Devi Nagar',
    'Divya Unnathi Layout',
    'Doctors Layout',
    'Dodda Banaswadi',
    'Dodda Kempaiah Layout',
    'Dodda Nekkundi',
    'Dodda Nekkundi Extension',
    'Doddaballapur',
    'Doddabanahalli',
    'Doddabidrakallu',
    'Doddabommasandra',
    'Doddagubbi',
    'Doddakallasandra',
    'Doddakammanahalli',
    'Doddakannelli',
    'Doddanakundi Industrial Area 2',
    'Doddanekundi',
    'Doddathoguru',
    'Dodsworth Layout',
    'Dollar Scheme Colony',
    'Dollars Colony',
    'Dollars Layout',
    'Domlur',
    'Domlur Layout',
    'Dommasandra',
    'Doopanahalli',
    'Dooravani Nagar',
    'Dr Shivarama Karantha Nagar',
    'ECC Road, Whitefield, ',
    'EPIP Zone',
    'Ejipura',
    'Electronic City',
    'Electronic City Phase II',
    'Electronic city Phase 1, ',
    'Electronics City Phase 1',
    'Esther Enclave Layout',
    'Ferrar Nagar',
    'Frazer Town',
    'Friends Colony',
    'GD Layout',
    'GM Palaya',
    'Ganesha Block',
    'Ganga Nagar',
    'Garebhavipalya',
    'Garudachar Palya',
    'Gattahalli',
    'Gattigere',
    'Geddalahalli',
    'Gidada Konnenahalli',
    'Giri Nagar',
    'Gkvk Layout',
    'Glass Factory Layout',
    'Gokula Extension',
    'Gollahalli',
    'Gollarapalya Hosahalli',
    'Gopalkrishna Nagar',
    'Gottigere',
    'Govindapura',
    'Govindaraja Nagar Ward',
    'Govindpura',
    'Green Domain Layout',
    'Green Garden Layout',
    'Green Glen Layout',
    'Green View Layout',
    'Green Woods Layout',
    'Gubbalala',
    'Guddadahalli',
    'Gulimangala',
    'Gunjur',
    'Gunjur Palya',
    'HAL 2nd Stage',
    'HAL 3rd Stage',
    'HBR Layout',
    'HMT Layout',
    'HOSUR MAIN ROAD',
    'HRBR Layout',
    'HSR Layout',
    'Hadosiddapura',
    'Hagadur',
    'Hanumanth Nagar',
    'Hanumantha Nagar',
    'Haralur Road',
    'Harappanahalli',
    'Harlur',
    'Hebbal',
    'Hebbal Kempapura',
    'Hegde Nagar',
    'Hennagara',
    'Hennur',
    'Hennur Bande',
    'Hennur Gardens',
    'Hennur Road',
    'Herohalli',
    'Hessarghatta',
    'Himagiri Meadows',
    'Hiremath Layout',
    'Hongasandra',
    'Hoodi',
    'Hoodi Circle, ',
    'Hoodi Layout',
    'Horamavu Agara',
    'Horamavu Banaswadi',
    'Hormavu',
    'Hosa Road',
    'Hosahalli Extension',
    'Hosakerehalli',
    'Hosakerehalli Layout',
    'Hoskote',
    'Hosur Road',
    'Hoysalanagar',
    'Hulimavu',
    'Huskur',
    'ISRO Layout',
    'ITI Layout',
    'ITPL',
    'Iblur Village',
    'Ilyas Nagar',
    'Immadihalli',
    'Indira Nagar',
    'Ittamadu',
    'J C Nagar',
    'JCR Layout',
    'JP Nagar',
    'JP Nagar 7th Phase, ',
    'Jai Bheema Nagar',
    'Jakkasandra Extension',
    'Jakkur',
    'Jakkur Plantation',
    'Jakkuru Layout',
    'Jalahalli',
    'Jalahalli East',
    'Jalahalli West',
    'Janatha Colony',
    'Jaya Mahal layout',
    'Jayamahal',
    'Jayanagar',
    'Jayanti Nagar',
    'Jeevan bima nagar',
    'Jigani',
    'Jinkethimmanahalli',
    'Jnana Ganga Nagar',
    'Jnanabharathi Layout',
    'Judicial Layout',
    'Judicial Layout, Kanakapura Road, ',
    'Jyothi Nagar',
    'KEB Colony',
    'KR Garden',
    'KR Puram',
    'KSRTC Layout',
    'KUDLU MAIN ROAD',
    'Kachanayakanahalli',
    'Kacharakanahalli',
    'Kada Agrahara',
    'Kadabagere',
    'Kadubeesanahalli',
    'Kadugodi',
    'Kadugondanahalli',
    'Kaggadasapura',
    'Kaggalipura',
    'Kaikondrahalli',
    'Kalena Agrahara',
    'Kalkere',
    'Kallumantapa',
    'Kalyan nagar',
    'Kamakshipalya',
    'Kamakya Layout',
    'Kamala Nagar',
    'Kambipura',
    'Kammagondahalli',
    'Kammanahalli',
    'Kammasandra',
    'Kanaka Nagar',
    'Kanakapura',
    'Kanakpura Road',
    'Kannamangala',
    'Kariyammana Agrahara',
    'Karuna Nagar',
    'Kasavanhalli',
    'Kashi Nagar',
    'Kasturi Nagar',
    'Kathriguppe',
    'Kattigenahalli',
    'Kaval Byrasandra',
    'Kaverappa Layout',
    'Kaveri Nagar',
    'Kavika Layout',
    'Kempegowda Nagar',
    'Kenchenahalli',
    'Kenchenhalli',
    'Kengeri',
    'Kengeri Hobli',
    'Kengeri Satellite Town',
    'Kereguddadahalli',
    'Keshava Nagar',
    'Kirloskar Layout',
    'Kithaganur',
    'Kodathi',
    'Kodbisanhalli',
    'Kodichikkanahalli',
    'Kodigehaali',
    'Kodigehalli',
    'Kodihalli',
    'Kodipalya',
    'Kogilu',
    'Konanakunte',
    'Konanakunte Cross',
    'Konena Agrahara',
    'Koramangala',
    'Kothannur',
    'Kothanur',
    'Kothnoor Dinne',
    'Krishna Nagar',
    'Krishna Reddy Layout',
    'Kudlu',
    'Kudlu Gate',
    'Kullappa Colony',
    'Kumara Park',
    'Kumarapalli',
    'Kumaraswami Layout',
    'Kumbena Agrahara',
    'Kundalahalli',
    'Kundalahalli Colony',
    'Kurubarahalli',
    'Kuvempu Nagar',
    'Kyalasanahalli',
    'LB Shastri Nagar',
    'Laggere',
    'Lake City',
    'Lakshmi Layout',
    'Lakshmiamma Garden',
    'Lakshminarayana Pura',
    'Lakshmipura',
    'Lal Bahadur Shastri Nagar',
    'Langford Town',
    'Lavakusha Nagar',
    'Lavelle Road',
    'Laxmi Sagar Layout',
    'Lingadheeranahalli',
    'Lingarajapuram',
    'Lottegolla Halli',
    'MCECHS  layout',
    'MLA Layout',
    'MS Pallya',
    'Madavara',
    'Madiwala',
    'Magadi Road',
    'Mahadevpura',
    'Mahaganapathy Nagar',
    'Mahalakshmi Layout',
    'Mahalakshmi Puram',
    'Maithri Layout',
    'Mallasandra',
    'Mallathahalli',
    'Malleshpalya',
    'Malleshwaram',
    'Manayata Tech Park',
    'Mangammanapalya',
    'Manjunath Nagar',
    'Manjunatha Layout',
    'Manorayana Palya',
    'Maragondanahalli',
    'Marasandra',
    'Marathahalli',
    'Margondanahalli',
    'Mariyannapalya',
    'Marsur',
    'Maruthi Nagar',
    'Maruthi Sevanagar',
    'Mathikere',
    'Mathikere Extension',
    'Medahalli',
    'Meenakunte',
    'Mico Layout',
    'Motappa Layout',
    'Muneshwara Nagar',
    'Munivenkatppa Layout',
    'Munnekollal',
    'Murugeshpalya',
    'Muthurayya Swamy Layout',
    'Mylasandra',
    'Mysore Road',
    'NGR Layout',
    'NRI Layout',
    'NS Palya',
    'Nagadevanahalli',
    'Naganathapura',
    'Nagappa Reddy Layout',
    'Nagaraja Garden',
    'Nagarbhavi',
    'Nagasandra',
    'Nagashetty Halli',
    'Nagavara',
    'Nagavarapalya',
    'Nagawara Junction',
    'Nagondanahalli',
    'Naidu Layout',
    'Nallurhalli',
    'Nandi Durga Road',
    'Nandini Layout',
    'Nanjappa Garden',
    'Nanjappa Layout',
    'Narayana Nagar 1st Block',
    'Narayanapura',
    'Nayandanahalli',
    'Near International Airport',
    'Neeladri Nagar',
    'Neelamangala',
    'Nehru Nagar',
    'Nelamangala',
    'New Gurappana Palya',
    'New Thippasandra',
    'Ngef Layout',
    'Nobo Nagar',
    'Nyanappana Halli',
    'OLd Gurappanapalya',
    'OMBR Layout',
    'Off Sarjapur Road, ',
    'Old Airport Road',
    'Old Madras Road',
    'Omarbagh Layout',
    'Omkar Nagar',
    'Outer Ring Road East',
    'P&T Layout',
    'Padmanabhanagar',
    'Pai Layout',
    'Palace Guttahalli',
    'Pampa Extension',
    'Panathur',
    'Parappana Agrahara',
    'Patelappa Layout',
    'Pattanagere',
    'Pattandur Agrahara',
    'Peenya',
    'Phase 1 Kammasandra',
    'Poorna Pragna Layout',
    'Poornapragna Housing Society Layout',
    'Pragathi Nagar',
    'Prashanth Nagar',
    'Prithvi Layout',
    'Puttanahalli',
    'R.T. Nagar',
    'RMV',
    'RMV 2nd Stage',
    'RMV Extension',
    'RMV Extension Stage 2',
    'RPC layout',
    'RR Layout',
    'RWF West Colony',
    'Rachenahalli',
    'Raghavendra Layout',
    'Raghavendra Nagar',
    'Raghuvanahalli',
    'Raja Rajeshwari Nagar',
    'Raja Rajeshwari Nagar 5th Stage',
    'Rajaji Nagar',
    'Rajarajeshwari Nagara',
    'Rajarajeshwari nagar',
    'Rajasree Layout',
    'Rajiv Gandhi Nagar',
    'Rajiv Nagar',
    'Ramagondanahalli',
    'Ramakrishnappa Layout',
    'Ramamurthy Nagar',
    'Ramamurthy Nagar Extension',
    'Ramanashree Enclave',
    'Ramanjaneyanagar',
    'Ramesh Nagar',
    'Rayasandra',
    'Reliaable Tranquil Layout',
    'Remco Bhel Layout',
    'Richards Town',
    'Richmond Town',
    'Roopena Agrahara',
    'Rustam Bagh Layout',
    'SMV layout',
    'SRINIVASAPURA',
    'Sadanand Nagar',
    'Sadaramangala',
    'Sadashiva Nagar',
    'Sahakara Nagar',
    'Sai Gardens',
    'Samethanahalli',
    'Sampangi Rama Nagar',
    'Sampigehalli',
    'Sanjay nagar',
    'Sarakki Nagar',
    'Sarjapur',
    'Sarjapur  Road',
    'Sarjapur Road, ',
    'Sarjapura - Attibele Road',
    'Sarvabhouma Nagar',
    'Sathya Layout',
    'Sector 1 HSR Layout',
    'Sector 2 HSR Layout',
    'Sector 6 HSR Layout',
    'Sector 7 HSR Layout',
    'Seegehalli',
    'Seetharampalya',
    'Seshadripuram',
    'Shampura',
    'Shankarapuram',
    'Shanthala Nagar',
    'Shanthi Layout',
    'Shanti Nagar',
    'Shantiniketan Layout',
    'Shikaripalya',
    'Shivaji Nagar',
    'Shree Ananth Nagar Layout',
    'Siddapura',
    'Sidedahalli',
    'Silk Board',
    'Silver Springs Layout',
    'Singanayakanahalli',
    'Singapura Village',
    'Singasandra',
    'Singena Agrahara',
    'Sneha Colony',
    'Somasundara Palya',
    'Someshwara Layout',
    'Sompura',
    'Sonnenahalli',
    'Soundarya Layout',
    'South',
    'Sri Balaji Krupa Layout',
    'Sri Venkateshpura Layout',
    'Srinagar',
    'Srinivasa Nagar',
    'Srirampura',
    'Srirampuram',
    'Stage-4 Bommanahalli',
    'Subash Nagar',
    'Subramanyapura',
    'Suddaguntepalya',
    'Sultan Palaya',
    'Sunder Ram Shetty Nagar',
    'Sunkadakatte',
    'Surabhi Layout',
    'Suraksha Nagar',
    'Syndicate Bank Colony',
    'T Dasarahalli',
    'T.C PALYA',
    'TC Palaya',
    'Tala Cauvery Layout',
    'Talaghattapura',
    'Tasker Town',
    'Tata Nagar',
    'Tavarekere',
    'Teachers Colony',
    'Tejaswini Nagar',
    'Telecom Layout',
    'Thanisandra',
    'Thanisandra Main Road, ',
    'Thanisandra main road',
    'Thigalarapalya',
    'Thirumenahalli',
    'Thubarahalli',
    'Thurahalli',
    'Thyagaraja Nagar',
    'Tigalarpalya',
    'Tindlu',
    'Tirumanahalli',
    'Tumkur Road',
    'Tunganagara',
    'Uday Nagar',
    'Udaya Nagar',
    'Udayapur Village',
    'Ullal Road',
    'Ullal Uppanagar',
    'Ulsoor',
    'Upadhyaya Layout',
    'Upkar Layout',
    'Uttarahalli',
    'VGP Layout',
    'VHBCS Layout',
    'Vadarpalya',
    'Vajarahalli',
    'Varanasi',
    'Varsova Layout',
    'Varthur',
    'Varthur Road',
    'Varthur Road, ',
    'Vasanth nagar',
    'Vasantha Vallabha Nagar',
    'Vasanthapura',
    'Vasanthpura',
    'Veer Sandra',
    'Veerannapalya',
    'Veersandra',
    'Venkatapura',
    'Venugopal Reddy Layout',
    'Versova Layout',
    'Vibhutipura Extension',
    'Vibuthipura',
    'Victoria Layout',
    'Vidyaranyapura',
    'Vignana Nagar',
    'Vijaya Bank Layout',
    'Vijayanagar',
    'Vijinapura',
    'Vimanapura',
    'Vinayak Nagar',
    'Vinayaka Nagar',
    'Virat Nagar',
    'Virupakshapura',
    'Vishveshwarya Layout',
    'Vishwanatha Nagenahalli',
    'Vishwapriya Layout',
    'Vishwapriya Nagar',
    'Vittal Nagar',
    'Vittasandra',
    'Volagerekallahalli',
    'Vyalikaval',
    'Whitefield',
    'Whitefield soukya road',
    'Wilson Garden',
    'Yarandahalli',
    'Yelachenahalli',
    'Yelahanka',
    'Yelahanka New Town',
    'Yelenahalli',
    'Yemlur',
    'Yeshwanthpur',
    'Yeshwanthpur Industrial Suburb',
    'cooketown',
    'frazertown',
    'manyata park',
    'others',
    'tc.palya'];

    const select = document.getElementById('location');

    locations.forEach(location => {
      const option = document.createElement('option');
      option.value = location;
      option.textContent = location;
      select.appendChild(option);
    });
  });

/*
document.getElementById('priceForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting and refreshing the page

    // Get form values
    const address = document.getElementById('address').value;
    const location = document.getElementById('location').value;
    const areaType = document.getElementById('areaType').value;
    const bedrooms = parseInt(document.getElementById('bedrooms').value, 10);
    const bathrooms = parseInt(document.getElementById('bathrooms').value, 10);
    const squareFeet = parseInt(document.getElementById('squareFeet').value, 10);
    const balcony = parseInt(document.getElementById('balcony').value, 10);

    // Basic pricing logic (Example, you should replace with real pricing model)
    let basePrice = 100000; // Base price in dollars
    let locationMultiplier = 1;
    if (location === 'city-center') locationMultiplier = 2.0;
    else if (location === 'suburbs') locationMultiplier = 1.5;
    else if (location === 'outskirts') locationMultiplier = 1.2;

    let areaMultiplier = 1;
    if (areaType === 'urban') areaMultiplier = 1.5;
    else if (areaType === 'suburban') areaMultiplier = 1.2;

    // Example price calculation
    let price = basePrice * locationMultiplier * areaMultiplier;
    price += bedrooms * 5000; // $5000 per bedroom
    price += bathrooms * 3000; // $3000 per bathroom
    price += squareFeet * 100; // $100 per square foot
    price += balcony * 50; // $50 per square foot of balcony

    // Display result
    document.getElementById('price').textContent = `$${price.toLocaleString()}`;
});
*/

document.getElementById('priceForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting and refreshing the page
  
    // Get form values and convert to appropriate types
    const location = document.getElementById('location').value;
    const areaType = document.getElementById('areaType').value;
    const bedrooms = parseInt(document.getElementById('bedrooms').value, 10);
    const bathrooms = parseInt(document.getElementById('bathrooms').value, 10);
    const squareFeet = parseInt(document.getElementById('squareFeet').value, 10);
    const balconies = parseInt(document.getElementById('balconies').value, 10);
  
    // Basic validation (optional but recommended)
    if (isNaN(bedrooms) || isNaN(bathrooms) || isNaN(squareFeet) || isNaN(balconies)) {
      alert('Please enter valid numbers for bedrooms, bathrooms, square feet, and balconies.');
      return;
    }
  
    // Send data to Flask server
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            location: location,
            areaType: areaType,
            bedrooms: bedrooms,
            bathrooms: bathrooms,
            squareFeet: squareFeet,
            balconies: balconies
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => Promise.reject(err));
        }
        return response.json();
    })
    .then(data => {
        // Display result
        document.getElementById('price').textContent = `₹${data.predicted_price.toLocaleString('en-IN')}`;
    })
    .catch(error => {
        console.error('Error:', error);
        // Optionally display an error message to the user
        document.getElementById('price').textContent = `Error: ${error.error || 'An unknown error occurred'}`;
    });
  });
  
  document.getElementById('clearButton').addEventListener('click', function() {
    // Clear the form fields
    document.getElementById('priceForm').reset();
    
    // Clear the displayed price
    document.getElementById('price').textContent = '₹0';
});