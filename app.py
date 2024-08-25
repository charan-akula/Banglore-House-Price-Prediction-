from flask import Flask, request, jsonify,render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)


    # Convert categorical features to numeric values (this is an example; adjust as necessary)
    location_map = {'Electronic City Phase II': 242,
 'Chikka Tirupathi': 175,
 'Uttarahalli': 680,
 'Lingadheeranahalli': 447,
 'Kothanur': 419,
 'Whitefield': 721,
 'Marathahalli': 472,
 '7th Phase JP Nagar': 32,
 'Gottigere': 266,
 'Sarjapur': 596,
 'Mysore Road': 490,
 'Bisuvanahalli': 142,
 'Raja Rajeshwari Nagar': 562,
 'Ramakrishnappa Layout': 571,
 'Manayata Tech Park': 465,
 'Binny Pete': 141,
 'Thanisandra': 659,
 'Bellandur': 127,
 'Mangammanapalya': 466,
 'Ramagondanahalli': 570,
 'Electronic City': 241,
 'Yelahanka': 726,
 'Hebbal': 294,
 'Kanakpura Road': 383,
 'Electronics City Phase 1': 244,
 'Kundalahalli': 430,
 'Chikkalasandra': 179,
 'Sarjapur  Road': 597,
 'Doddathoguru': 227,
 'Himagiri Meadows': 304,
 'others': 735,
 'Bhoganhalli': 133,
 'Lakshminarayana Pura': 440,
 'Begur Road': 124,
 'Murugeshpalya': 487,
 'Govindaraja Nagar Ward': 268,
 'Ganga Nagar': 252,
 'Varthur': 687,
 'Gunjur': 278,
 'Hegde Nagar': 296,
 'Haralur Road': 291,
 'Hennur Road': 301,
 'Kothannur': 418,
 'Kalena Agrahara': 370,
 'Cholanayakanahalli': 184,
 'Garudachar Palya': 254,
 'EPIP Zone': 239,
 'Dasanapura': 199,
 'Kasavanhalli': 387,
 'Rajaji Nagar': 564,
 'Sanjay nagar': 594,
 'ISRO Layout': 322,
 'Domlur': 232,
 'Kengeri': 399,
 'Sarjapura - Attibele Road': 599,
 'Devasthanagalu': 209,
 'T Dasarahalli': 648,
 'Yeshwanthpur': 730,
 'Green View Layout': 273,
 'Shantiniketan Layout': 614,
 'Peenya': 542,
 'Nagarbhavi': 498,
 'Jalahalli West': 341,
 'Devanahalli': 204,
 'Lakshmiamma Garden': 439,
 'Byatarayanapura': 154,
 'Ramamurthy Nagar': 572,
 'Malleshwaram': 464,
 'Akshaya Nagar': 45,
 'Shampura': 609,
 'Kadugodi': 365,
 'LB Shastri Nagar': 435,
 'Vajarahalli': 684,
 'Hormavu': 312,
 'Vishwapriya Layout': 715,
 'Kudlu Gate': 424,
 '8th Phase JP Nagar': 34,
 'Bommasandra Industrial Area': 145,
 'Chandra Layout': 167,
 'Anandapura': 61,
 'Kengeri Satellite Town': 401,
 'Basavanapura': 117,
 'Kannamangala': 384,
 ' Devarachikkanahalli': 1,
 'Hulimavu': 320,
 'Mahalakshmi Layout': 458,
 'Yarandahalli': 724,
 'Hosa Road': 313,
 'Keshava Nagar': 403,
 'RMV Extension': 553,
 'Tejaswini Nagar': 657,
 'Jai Bheema Nagar': 334,
 'CV Raman Nagar': 158,
 'Kumaraswami Layout': 428,
 'Hebbal Kempapura': 295,
 'Vijayanagar': 706,
 '8th block Koramangala': 35,
 'Jakkuru Layout': 338,
 'KR Puram': 357,
 'Pattandur Agrahara': 541,
 'Ejipura': 240,
 'MS Pallya': 452,
 'HSR Layout': 286,
 'Nagasandra': 499,
 'Langford Town': 443,
 'Kogilu': 413,
 'Panathur': 537,
 'Nagondanahalli': 504,
 'Padmanabhanagar': 533,
 '1st Block Jayanagar': 6,
 'Kammasandra': 380,
 'Off Sarjapur Road, ': 526,
 'Tala Cauvery Layout': 651,
 'Dasarahalli': 201,
 'Magadi Road': 455,
 'Ngef Layout': 521,
 'Koramangala': 417,
 'Muthurayya Swamy Layout': 488,
 'Dommasandra': 234,
 'Budigere': 151,
 'Dodda Nekkundi Extension': 216,
 'Mylasandra': 489,
 'Kalyan nagar': 373,
 'Dr Shivarama Karantha Nagar': 237,
 'Bank Of Baroda Colony': 111,
 'Kullappa Colony': 425,
 'Ashwath Nagar': 76,
 'OMBR Layout': 525,
 'Anand Nagar': 59,
 'Shree Ananth Nagar Layout': 617,
 'Kundalahalli Colony': 431,
 'Horamavu Agara': 310,
 'Coffee Board Layout': 190,
 'Ambedkar Nagar': 55,
 'Attibele': 79,
 'KUDLU MAIN ROAD': 359,
 'Talaghattapura': 652,
 'Balagere': 102,
 'Jigani': 348,
 'Gollarapalya Hosahalli': 264,
 'Srirampura': 636,
 'Old Madras Road': 528,
 'Kaggadasapura': 367,
 'Silver Springs Layout': 621,
 'Chandapura': 166,
 '9th Phase JP Nagar': 37,
 'Jakkur': 336,
 'TC Palaya': 650,
 'Maruthi Sevanagar': 477,
 'RMV 2nd Stage': 552,
 'Giri Nagar': 259,
 'Singasandra': 624,
 'AECS Layout': 39,
 'Mallasandra': 461,
 'Begur': 123,
 'JP Nagar': 332,
 'Sunder Ram Shetty Nagar': 643,
 'Malleshpalya': 463,
 'Kodathi': 406,
 'Munnekollal': 486,
 'Motappa Layout': 483,
 'Akshaya Vana': 46,
 'Kaval Byrasandra': 392,
 'Kaggalipura': 368,
 'Basavanna Nagar': 119,
 '6th Phase JP Nagar': 29,
 'Ulsoor': 677,
 'Thigalarapalya': 662,
 'Somasundara Palya': 627,
 'T.C PALYA': 649,
 'Muneshwara Nagar': 484,
 'Basaveshwara Nagar': 120,
 'Bommasandra': 144,
 'Prashanth Nagar': 547,
 'Ardendale': 72,
 'Harlur': 293,
 'Sampigehalli': 593,
 'RMV': 551,
 'Bagalur Main Road': 101,
 'Kodihalli': 411,
 'Narayanapura': 512,
 'Hennur': 298,
 '5th Phase JP Nagar': 27,
 'Kodigehaali': 409,
 'Bannerghatta Road': 113,
 'Billekahalli': 140,
 'Jalahalli': 339,
 'Hoodi Circle, ': 308,
 'Sompura': 629,
 'Ashirvad Colony': 75,
 'Dodda Nekkundi': 215,
 'Hosur Road': 318,
 'Battarahalli': 122,
 'Gokula Extension': 262,
 'Kamakshipalya': 374,
 'Ambalipura': 53,
 'Hoodi': 307,
 'Samethanahalli': 591,
 'Brookefield': 150,
 'Yelenahalli': 728,
 'Suddaguntepalya': 641,
 'Udayapur Village': 674,
 'Vittasandra': 718,
 'Hoysalanagar': 319,
 'Defence Colony': 202,
 '2nd Stage Nagarbhavi': 16,
 'Vidyaranyapura': 703,
 'Amruthahalli': 57,
 'Kodigehalli': 410,
 'Patelappa Layout': 539,
 'NS Palya': 493,
 'Subramanyapura': 640,
 'Basavangudi': 118,
 '3rd Block Hrbr Layout': 18,
 'Surabhi Layout': 645,
 'Banjara Layout': 110,
 'Omkar Nagar': 530,
 'Kereguddadahalli': 402,
 'Maragondanahalli': 470,
 'Silk Board': 620,
 'Kada Agrahara': 362,
 'Kambipura': 377,
 'BHEL Layout': 90,
 'Kashi Nagar': 388,
 'Sector 7 HSR Layout': 605,
 'VHBCS Layout': 682,
 'Rajiv Nagar': 569,
 'Gattahalli': 255,
 'Arekere': 74,
 'Ramanjaneyanagar': 575,
 '7th Block Jayanagar': 31,
 '2nd Phase JP Nagar': 13,
 'Kammanahalli': 379,
 'Banashankari': 104,
 'Chikkabanavar': 176,
 'Ittamadu': 329,
 'HRBR Layout': 285,
 'Banashankari Stage III': 106,
 'Dooravani Nagar': 236,
 'JCR Layout': 331,
 'Nehru Nagar': 517,
 'Kanakapura': 382,
 'Sneha Colony': 626,
 'Konanakunte': 414,
 'Doddagubbi': 221,
 'Sector 6 HSR Layout': 604,
 'Margondanahalli': 473,
 'ITI Layout': 323,
 'R.T. Nagar': 550,
 'Tumkur Road': 670,
 'Vasanthapura': 692,
 'GM Palaya': 250,
 'Mahadevpura': 456,
 'Poornapragna Housing Society Layout': 545,
 'Hosakerehalli': 315,
 'Huskur': 321,
 'Indira Nagar': 328,
 'Shanthala Nagar': 611,
 'Herohalli': 302,
 'Teachers Colony': 656,
 'Srinivasa Nagar': 635,
 'Byrathi Village': 156,
 'Kodichikkanahalli': 408,
 'Ambedkar Colony': 54,
 'Varthur Road': 688,
 'Anjappa Layout': 68,
 'Avalahalli': 82,
 'Anjanapura': 67,
 'Abbigere': 43,
 'Tindlu': 668,
 'B Narayanapura': 85,
 'Green Garden Layout': 271,
 'Gubbalala': 275,
 'Dairy Circle': 198,
 'Parappana Agrahara': 538,
 'Jeevan bima nagar': 347,
 'Narayana Nagar 1st Block': 511,
 'KSRTC Layout': 358,
 'Anekal': 65,
 'New Gurappana Palya': 519,
 'Vadarpalya': 683,
 'Kudlu': 423,
 'Old Airport Road': 527,
 'Banashankari Stage VI': 108,
 'HMT Layout': 283,
 'Cox Town': 193,
 'Kathriguppe': 390,
 'HBR Layout': 282,
 'Richmond Town': 581,
 'Sahakara Nagar': 589,
 'manyata park': 734,
 'Rachenahalli': 558,
 'Sadashiva Nagar': 588,
 'Yelachenahalli': 725,
 'Kodbisanhalli': 407,
 'Kasturi Nagar': 389,
 'Vishwanatha Nagenahalli': 714,
 'Bendiganahalli': 129,
 'Hosakerehalli Layout': 316,
 'Hennagara': 297,
 'Ferrar Nagar': 246,
 'Green Glen Layout': 272,
 'Thubarahalli': 664,
 'Naganathapura': 495,
 'Basavanagara': 116,
 'Horamavu Banaswadi': 311,
 '1st Phase JP Nagar': 8,
 'Kaverappa Layout': 393,
 'NGR Layout': 491,
 'Divya Unnathi Layout': 211,
 'Vasantha Vallabha Nagar': 691,
 'Seegehalli': 606,
 'BEML Layout': 89,
 'NRI Layout': 492,
 'Sidedahalli': 619,
 'ITPL': 324,
 'Thurahalli': 665,
 'Raghavendra Nagar': 560,
 'Babusapalaya': 97,
 'Nagappa Reddy Layout': 496,
 'BTM 1st Stage': 92,
 'Kariyammana Agrahara': 385,
 'Hessarghatta': 303,
 'Suraksha Nagar': 646,
 'Iblur Village': 325,
 'Kadugondanahalli': 366,
 'Basava Nagar': 115,
 '2nd Block Hrbr Layout': 11,
 'Canara Bank Layout': 161,
 'Manjunath Nagar': 467,
 'Basapura': 114,
 'Channasandra': 168,
 'Singena Agrahara': 625,
 'Jalahalli East': 340,
 'Gopalkrishna Nagar': 265,
 'Choodasandra': 185,
 'Sai Gardens': 590,
 'Dodda Kempaiah Layout': 214,
 'Hanumanth Nagar': 289,
 'Kaikondrahalli': 369,
 'RWF West Colony': 557,
 'Neeladri Nagar': 515,
 'Frazer Town': 247,
 'Doddakallasandra': 222,
 'Chamrajpet': 164,
 'VGP Layout': 681,
 'Classic Paradise Layout': 186,
 'Vasanth nagar': 690,
 'Rayasandra': 577,
 'Kalkere': 371,
 'Vibuthipura': 701,
 '5th Block Hbr Layout': 26,
 'Pai Layout': 534,
 'Roopena Agrahara': 582,
 'Banashankari Stage V': 107,
 'Coconut Garden': 188,
 'Gollahalli': 263,
 'Sonnenahalli': 630,
 'Bommanahalli': 143,
 'ECC Road, Whitefield, ': 238,
 'Seetharampalya': 607,
 'Devanahalli Int. Airport': 205,
 'Puttanahalli': 549,
 'Devasandra Extension': 208,
 '2nd Phase Judicial Layout': 14,
 'Sarjapur Road, ': 598,
 'Byadarahalli': 152,
 'Poorna Pragna Layout': 544,
 'Judicial Layout': 352,
 'Varthur Road, ': 689,
 'Chikka Banaswadi': 174,
 'Outer Ring Road East': 531,
 'Kavika Layout': 395,
 'Vinayaka Nagar': 710,
 'Banashankari Stage II': 105,
 'AMS Layout': 41,
 'Ashwathnagar': 77,
 'AGS Layout': 40,
 'Srinagar': 634,
 'Bannerghatta': 112,
 'Belathur': 125,
 'Devanahalli Road': 206,
 'Green Woods Layout': 274,
 'Immadihalli': 327,
 'Banagiri Nagar': 103,
 'Ananth Nagar': 63,
 'Hiremath Layout': 305,
 'Jnanabharathi Layout': 351,
 'Chikkasandra': 180,
 '3rd Block Jayanagar': 19,
 'Manjunatha Layout': 468,
 'Abbaiah Reddy Layout': 42,
 'Lakshmi Layout': 438,
 'Tavarekere': 655,
 'Thirumenahalli': 663,
 'HOSUR MAIN ROAD': 284,
 'Nandi Durga Road': 507,
 'Cooke Town': 191,
 'Daadys Gaarden Layout': 197,
 'Maruthi Nagar': 476,
 'Marsur': 475,
 'Karuna Nagar': 386,
 'Kallumantapa': 372,
 'Medahalli': 480,
 'Rustam Bagh Layout': 583,
 'New Thippasandra': 520,
 'Kumbena Agrahara': 429,
 'frazertown': 733,
 'Akshayanagara East': 47,
 'Doddanekundi': 226,
 'Bommenahalli': 146,
 'Mahaganapathy Nagar': 457,
 'Kattigenahalli': 391,
 'Andrahalli': 64,
 'Vittal Nagar': 717,
 '3rd Block Banashankari': 17,
 'Bhuvaneshwari Nagar': 135,
 'Victoria Layout': 702,
 'Prithvi Layout': 548,
 '5th Stage BEML Layout': 28,
 'Jaya Mahal layout': 343,
 'BSM Extension': 91,
 'Vijinapura': 707,
 'Banaswadi': 109,
 'P&T Layout': 532,
 'Byrasandra': 155,
 'Mathikere Extension': 479,
 'Sector 2 HSR Layout': 603,
 'Shivaji Nagar': 616,
 'Badavala Nagar': 98,
 '4th Block Koramangala': 23,
 'Belatur': 126,
 'Kamakya Layout': 375,
 'Vignana Nagar': 704,
 'Nallurhalli': 506,
 'Chinnapanahalli': 183,
 'Lingarajapuram': 448,
 'Laxmi Sagar Layout': 446,
 'Nagavarapalya': 502,
 'Hongasandra': 306,
 'Harappanahalli': 292,
 'BTM Layout': 95,
 'Chennammana Kere': 171,
 'Tasker Town': 653,
 'Kumara Park': 426,
 'BEL Road': 88,
 'Byagadadhenahalli': 153,
 'Doddabommasandra': 220,
 'Tunganagara': 671,
 'BTM 2nd Stage': 93,
 'Remco Bhel Layout': 579,
 'Sri Venkateshpura Layout': 633,
 'Jakkur Plantation': 337,
 'Bikasipura': 138,
 '1st Block Koramangala': 7,
 'Hoskote': 317,
 'Yemlur': 729,
 'Gkvk Layout': 260,
 'Sector 1 HSR Layout': 602,
 'Laggere': 436,
 'Doopanahalli': 235,
 'Doddaballapur': 217,
 'Nelamangala': 518,
 'Alfa Garden Layout': 50,
 'Mico Layout': 482,
 'Hoodi Layout': 309,
 'Gunjur Palya': 279,
 'Bileshivale': 139,
 'Sunkadakatte': 644,
 'Someshwara Layout': 628,
 'Kacharakanahalli': 361,
 'Channasandra Layout': 169,
 'HAL 3rd Stage': 281,
 'Nagavara': 501,
 'Doctors Layout': 212,
 'Vishwapriya Nagar': 716,
 'Sarakki Nagar': 595,
 'Nandini Layout': 508,
 'Vibhutipura Extension': 700,
 'B Channasandra': 84,
 'Dollars Colony': 230,
 'Arehalli': 73,
 'Hennur Gardens': 300,
 'Veerannapalya': 695,
 'Bharathi Nagar': 132,
 'SRINIVASAPURA': 585,
 'Cambridge Layout': 159,
 'Doddakannelli': 224,
 'Vishveshwarya Layout': 713,
 'Thanisandra Main Road, ': 660,
 'Jayanagar': 345,
 'Amruthnagar': 58,
 'Akshya Nagar': 49,
 'Benson Town': 130,
 'BCC Layout': 86,
 'Mathikere': 478,
 'Friends Colony': 248,
 'Doddabidrakallu': 219,
 'Bidadi': 137,
 'Rajiv Gandhi Nagar': 568,
 'Kengeri Hobli': 400,
 'Vyalikaval': 720,
 'HAL 2nd Stage': 280,
 ' Devarabeesana Halli': 0,
 '1st Block HRBR Layout': 5,
 '1st Stage Indira Nagar': 9,
 'Shanthi Layout': 612,
 'Esther Enclave Layout': 245,
 'Shikaripalya': 615,
 '4th T block Jayanagar': 25,
 'Nayandanahalli': 513,
 'Sultan Palaya': 642,
 'Hagadur': 288,
 'Soundarya Layout': 631,
 'Yelahanka New Town': 727,
 'Amarjyothi Colony': 52,
 'Pattanagere': 540,
 'Cunningham Road': 195,
 'Dollars Layout': 231,
 'Basaveshwara Nagar Yelahanka': 121,
 'Bhuvaneswari Nagar': 136,
 'Varanasi': 685,
 'Virat Nagar': 711,
 'Chennammanakere Achukattu': 172,
 'Volagerekallahalli': 719,
 'Nobo Nagar': 522,
 'Govindpura': 269,
 'Kadubeesanahalli': 364,
 'Green Domain Layout': 270,
 'Cleveland Town': 187,
 'Syndicate Bank Colony': 647,
 'Bellari Road': 128,
 'Jyothi Nagar': 354,
 'Tata Nagar': 654,
 'Tirumanahalli': 669,
 'MCECHS  layout': 450,
 'Geddalahalli': 257,
 'Brindavan Nagar': 148,
 'Mariyannapalya': 474,
 'Kanaka Nagar': 381,
 'Domlur Layout': 233,
 'Vijaya Bank Layout': 705,
 'Raghuvanahalli': 561,
 'Wilson Garden': 723,
 'Challaghatta': 163,
 'Nyanappana Halli': 523,
 'KR Garden': 356,
 'Mallathahalli': 462,
 'Thyagaraja Nagar': 666,
 'Bagalur': 100,
 'Crimson Layout': 194,
 'Hanumantha Nagar': 290,
 'Lavelle Road': 445,
 'MLA Layout': 451,
 'Kyalasanahalli': 434,
 'Siddapura': 618,
 'Nagadevanahalli': 494,
 'Madiwala': 454,
 'Rajarajeshwari Nagara': 565,
 'Munivenkatppa Layout': 485,
 'Kamala Nagar': 376,
 'Kumarapalli': 427,
 'Nagawara Junction': 503,
 'Maithri Layout': 460,
 'Raja Rajeshwari Nagar 5th Stage': 563,
 'Nanjappa Garden': 509,
 'Kenchenhalli': 398,
 'Hadosiddapura': 287,
 'Kachanayakanahalli': 360,
 'Nagaraja Garden': 497,
 '6th block Koramangala': 30,
 '4th Block Jayanagar': 22,
 'Canara Bank Colony': 160,
 'Seshadripuram': 608,
 'Akshayanagara West': 48,
 'Anand nagar': 60,
 'SMV layout': 584,
 'Bagalakunte': 99,
 'OLd Gurappanapalya': 524,
 'Chikkadunnasandra': 177,
 'Gattigere': 256,
 'Cottonpet': 192,
 'Sampangi Rama Nagar': 592,
 'Pragathi Nagar': 546,
 'A Narayanapura': 38,
 'Kenchenahalli': 397,
 'Amblipura': 56,
 'Rajarajeshwari nagar': 566,
 'Jinkethimmanahalli': 349,
 'Vimanapura': 708,
 'Dodsworth Layout': 228,
 'CQAL Layout': 157,
 'Venugopal Reddy Layout': 698,
 'Lake City': 437,
 'Lakshmipura': 441,
 'GD Layout': 249,
 'Kithaganur': 405,
 'JP Nagar 7th Phase, ': 333,
 'J C Nagar': 330,
 'Doddakammanahalli': 223,
 'Chikkathoguru': 181,
 'Richards Town': 580,
 'Manorayana Palya': 469,
 'Vinayak Nagar': 709,
 'Mahalakshmi Puram': 459,
 'Attur Layout': 80,
 'Brooke Bond First Cross': 149,
 'Glass Factory Layout': 261,
 'Chikkakannalli': 178,
 'Upkar Layout': 679,
 'Yeshwanthpur Industrial Suburb': 731,
 'Thanisandra main road': 661,
 'Doddabanahalli': 218,
 'D Group Employees Layout': 196,
 'Whitefield soukya road': 722,
 'Kempegowda Nagar': 396,
 '4th Phase JP Nagar': 24,
 'Singanayakanahalli': 622,
 'Venkatapura': 697,
 'Ilyas Nagar': 326,
 '3rd Phase JP Nagar': 21,
 'Reliaable Tranquil Layout': 578,
 'Lottegolla Halli': 449,
 'Chelekare': 170,
 '8th Block Jayanagar': 33,
 'Atmananda Colony': 78,
 'Baba Nagar': 96,
 'Lal Bahadur Shastri Nagar': 442,
 'Kurubarahalli': 432,
 'Palace Guttahalli': 535,
 'Bethel Nagar': 131,
 'Kirloskar Layout': 404,
 'tc.palya': 736,
 'Dollar Scheme Colony': 229,
 'Konanakunte Cross': 415,
 'Omarbagh Layout': 529,
 'Kodipalya': 412,
 'Aishwarya Crystal Layout': 44,
 '2nd Block Jayanagar': 12,
 'Subash Nagar': 639,
 'Austin Town': 81,
 'Carmelaram': 162,
 'Hennur Bande': 299,
 '1st Block BEL Layout': 3,
 'Anantapura': 62,
 'Hosahalli Extension': 314,
 'Singapura Village': 623,
 'Marasandra': 471,
 'Ullal Uppanagar': 676,
 ' south': 2,
 '3rd Block Koramangala': 20,
 'Jakkasandra Extension': 335,
 'Ganesha Block': 251,
 'Gidada Konnenahalli': 258,
 'Near International Airport': 514,
 'Dasappa Layout': 200,
 'BTM 4th Stage': 94,
 'Chamundi Nagar': 165,
 'Udaya Nagar': 673,
 'Ullal Road': 675,
 'Krishna Reddy Layout': 422,
 'Kaveri Nagar': 394,
 'Devi Nagar': 210,
 'Jnana Ganga Nagar': 350,
 'Stage-4 Bommanahalli': 638,
 'Judicial Layout, Kanakapura Road, ': 353,
 'Srirampuram': 637,
 'Sathya Layout': 601,
 'Shanti Nagar': 613,
 '2nd Stage Arekere Mico Layout': 15,
 'Jayamahal': 344,
 'Veer Sandra': 694,
 'Chennappa Layout': 173,
 'RMV Extension Stage 2': 554,
 'Sadanand Nagar': 586,
 'Lavakusha Nagar': 444,
 'Dena Bank Colony': 203,
 'Kadabagere': 363,
 '1st Block HBR Layout': 4,
 'Kothnoor Dinne': 420,
 'Guddadahalli': 276,
 'Vasanthpura': 693,
 'Ramesh Nagar': 576,
 'Sarvabhouma Nagar': 600,
 'Virupakshapura': 712,
 'Coconut Grove Layout': 189,
 'RR Layout': 556,
 'Anjana Nagar': 66,
 'Janatha Colony': 342,
 'Veersandra': 696,
 'Tigalarpalya': 667,
 '2nd Block Bel Layout': 10,
 'Ramamurthy Nagar Extension': 573,
 'Ankappa Layout': 69,
 'Upadhyaya Layout': 678,
 'Meenakunte': 481,
 'Pampa Extension': 536,
 'Doddanakundi Industrial Area 2': 225,
 'Shankarapuram': 610,
 'Krishna Nagar': 421,
 'Nanjappa Layout': 510,
 'BCMC Layout': 87,
 'Uday Nagar': 672,
 'Telecom Layout': 658,
 'Nagashetty Halli': 500,
 'Electronic city Phase 1, ': 243,
 'Naidu Layout': 505,
 'Devara Jeevanahalli': 207,
 'Anugrah Layout': 71,
 'Annapurneshwari Nagar': 70,
 'RPC layout': 555,
 'Gulimangala': 277,
 'Sadaramangala': 587,
 'Konena Agrahara': 416,
 'Raghavendra Layout': 559,
 'Varsova Layout': 686,
 'Phase 1 Kammasandra': 543,
 'KEB Colony': 355,
 'Rajasree Layout': 567,
 'Madavara': 453,
 'Garebhavipalya': 253,
 'Neelamangala': 516,
 'Brindavan Layout': 147,
 'Dodda Banaswadi': 213,
 'cooketown': 732,
 'Jayanti Nagar': 346,
 'Ramanashree Enclave': 574,
 'Chikku Lakshmaiah Layout': 182,
 '9th Block Jayanagar': 36,
 'Kammagondahalli': 378,
 'Govindapura': 267,
 'Bhoopsandra': 134,
 'Kuvempu Nagar': 433,
 'Sri Balaji Krupa Layout': 632,
 'Ayappa Nagar': 83,
 'Amam Enclave Layout': 51,
 'Versova Layout': 699}

    area_type_map = {'Super Built-up Area': 3,
 'Plot Area': 2,
 'Built-up Area': 0,
 'Carpet Area': 1}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from the request
        data = request.get_json()  # Use get_json() for better error handling
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        location = data.get('location')
        area_type = data.get('areaType')
        bedrooms = int(data.get('bedrooms', 0))  # Provide default values
        bathrooms = int(data.get('bathrooms', 0))
        squareFeet = int(data.get('squareFeet', 0))
        balconies = int(data.get('balconies', 0))

        # Validate and preprocess input data
        if location not in location_map:
            return jsonify({'error': 'Invalid location'}), 400
        if area_type not in area_type_map:
            return jsonify({'error': 'Invalid area type'}), 400
        if (squareFeet<300 or squareFeet>30000):
            return jsonify({'error':'out of limit'}), 400

        location_encoded = location_map[location]
        area_type_encoded = area_type_map[area_type]

        # Prepare the feature vector
        features = np.array([location_encoded,squareFeet,area_type_encoded, bedrooms, bathrooms, balconies]).reshape(1, -1)

        # Predict using the model
        prediction = model.predict(features)

        return jsonify({'predicted_price': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    
if __name__ == '__main__':
    app.run(debug=True)