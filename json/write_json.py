import json

visits = [
  {
    "url": "https://dev1-pwa.croma.com/cart",
    "customerHash": "7e4af5771224af470d01157a988b8b96",
    "createdAt": "2025-06-11 07:04:29.336000 UTC"
  },
  {
    "url": "/home",
    "customerHash": "88642ef3c27d9f497be2389e765bdedc",
    "createdAt": "2025-06-11 07:05:27.243000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/hamburger-menu/logged-in/5_5",
    "customerHash": "d8e3ec16aa0484f4427940bc86f3c616",
    "createdAt": "2025-06-11 07:07:47.850000 UTC"
  },
  {
    "url": "http://localhost:3000/en-in/bookings/landing-page?hotelId\u003d26fb307e-87e3-4bde-ad1c-c9e95ea3ea62",
    "customerHash": "",
    "createdAt": "2025-06-11 07:08:09.385000 UTC"
  },
  {
    "url": "http://localhost:3000/en-in/bookings/landing-page?hotelId\u003d26fb307e-87e3-4bde-ad1c-c9e95ea3ea62",
    "customerHash": "",
    "createdAt": "2025-06-11 07:08:25.226000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/tsss/email-verify",
    "customerHash": "99b84ae63a658bdb10f7e23e44d0d34b",
    "createdAt": "2025-06-11 07:08:36.611000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/auth/login",
    "customerHash": "",
    "createdAt": "2025-06-11 07:08:55.298000 UTC"
  },
  {
    "url": "/hamburger-menu/logged-in/5_5",
    "customerHash": "c184408505208427d056967d3942996d",
    "createdAt": "2025-06-11 07:09:57.198000 UTC"
  },
  {
    "url": "/auth/login",
    "customerHash": "",
    "createdAt": "2025-06-11 07:10:04.868000 UTC"
  },
  {
    "url": "/auth/login",
    "customerHash": "",
    "createdAt": "2025-06-11 07:10:33.467000 UTC"
  },
  {
    "url": "https://stg.titan.co.in/shop/watches-for-women?lang\u003den_IN",
    "customerHash": "",
    "createdAt": "2025-06-11 07:10:34.019000 UTC"
  },
  {
    "url": "/fs-slp/insurance",
    "customerHash": "e381bdca90430ead04884d78832aabba",
    "createdAt": "2025-06-11 07:11:36.756000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/hamburger-menu/logged-in/5_5",
    "customerHash": "c77afd06ae36f143b63d1ebfd8d9f4d8",
    "createdAt": "2025-06-11 07:11:50.373000 UTC"
  },
  {
    "url": "/fixed-deposit/home-redirection?utm_source\u003dPaidMarketing\u0026utm_medium\u003dAPP\u0026utm_campaign\u003dCategories\u0026utm_content\u003dAPP\u0026utm_term\u003dPaidMarketing",
    "customerHash": "503187f3a881255ca2ff007f161a5627",
    "createdAt": "2025-06-11 07:13:27.571000 UTC"
  },
  {
    "url": "/fixed-deposit/discovery-redirection?utm_source\u003dPaidMarketing\u0026utm_medium\u003dAPP\u0026utm_campaign\u003dCategories\u0026utm_content\u003dAPP\u0026utm_term\u003dPaidMarketing",
    "customerHash": "503187f3a881255ca2ff007f161a5627",
    "createdAt": "2025-06-11 07:13:35.848000 UTC"
  },
  {
    "url": "https://stg.fastrack.in/shop/watches?srule\u003dprice-high-to-low\u0026start\u003d0\u0026sz\u003d48\u0026lang\u003den_IN",
    "customerHash": "",
    "createdAt": "2025-06-11 07:13:43.294000 UTC"
  },
  {
    "url": "/fixed-deposit/discovery-redirection?utm_source\u003dPaidMarketing\u0026utm_medium\u003dAPP\u0026utm_campaign\u003dCategories\u0026utm_content\u003dAPP\u0026utm_term\u003dPaidMarketing",
    "customerHash": "503187f3a881255ca2ff007f161a5627",
    "createdAt": "2025-06-11 07:13:49.965000 UTC"
  },
  {
    "url": "",
    "customerHash": "616247a3f788640bf547c084bc938032",
    "createdAt": "2025-06-11 07:15:08.643000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/home",
    "customerHash": "53920bc6f4db55fcc1dee7927b0c3677",
    "createdAt": "2025-06-11 07:16:31.021000 UTC"
  },
  {
    "url": "http://localhost:3000/en-in/hotels",
    "customerHash": "",
    "createdAt": "2025-06-11 07:16:50.828000 UTC"
  },
  {
    "url": "/motor/2w/buy-plan",
    "customerHash": "da9a09e9d4452339bf6a8cb4b176a50e",
    "createdAt": "2025-06-11 07:17:14.851000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/neupass",
    "customerHash": "95dbaad7ea372ca286843c5980e469b7",
    "createdAt": "2025-06-11 07:17:35.303000 UTC"
  },
  {
    "url": "https://stag.1mg.com/search/all?filter\u003dtrue\u0026name\u003dHorlicks",
    "customerHash": "5d5adda73cff2cd72dc15479cc924bc2",
    "createdAt": "2025-06-11 07:18:56.459000 UTC"
  },
  {
    "url": "https://stag.1mg.com/search/all?filter\u003dtrue\u0026name\u003dHorlicks",
    "customerHash": "5d5adda73cff2cd72dc15479cc924bc2",
    "createdAt": "2025-06-11 07:18:56.522000 UTC"
  },
  {
    "url": "/fs-slp/insurance",
    "customerHash": "e381bdca90430ead04884d78832aabba",
    "createdAt": "2025-06-11 07:18:56.533000 UTC"
  },
  {
    "url": "http://localhost:3333/nearbyStoreList",
    "customerHash": "",
    "createdAt": "2025-06-11 07:18:59.049000 UTC"
  },
  {
    "url": "https://stg.tanishq.co.in/cart?lang\u003den_IN",
    "customerHash": "d6770c4f390b9e27806231ad3401d8c6",
    "createdAt": "2025-06-11 07:19:32.533000 UTC"
  },
  {
    "url": "/finance/investment-referral/share-referral-code-bottom-sheet",
    "customerHash": "b0b7f7c22df0ff5ecdc41f6bdbbb40f8",
    "createdAt": "2025-06-11 07:21:06.192000 UTC"
  },
  {
    "url": "/offers/zone",
    "customerHash": "77b5970f785b4b2641aa4359fa186598",
    "createdAt": "2025-06-11 07:22:40.772000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/offers/zone/tsss/employee-zone",
    "customerHash": "ff495d13dda828fae89bde8189aea1e1",
    "createdAt": "2025-06-11 07:22:44.940000 UTC"
  },
  {
    "url": "https://stg.titan.co.in/shop/watches?lang\u003den_IN\u0026start\u003d0\u0026sz\u003d24",
    "customerHash": "1ccc2e546a7de1d19742a9848deea5b5",
    "createdAt": "2025-06-11 07:22:50.255000 UTC"
  },
  {
    "url": "https://preprod2.tataunistore.com/checkout",
    "customerHash": "78855d2eba3ca7a147351ae83c192674",
    "createdAt": "2025-06-11 07:23:26.211000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/home",
    "customerHash": "c9843a19f556dcfcd7eac4c4c27be3e7",
    "createdAt": "2025-06-11 07:23:42.376000 UTC"
  },
  {
    "url": "http://localhost:3333/nearbyStoreList",
    "customerHash": "",
    "createdAt": "2025-06-11 07:23:51.895000 UTC"
  },
  {
    "url": "https://preprod-pwa.croma.com/cart",
    "customerHash": "4e9ff813f9d198b2321a08837bfb61e7",
    "createdAt": "2025-06-11 07:25:14.679000 UTC"
  },
  {
    "url": "/finance/insurance/life/dynamicPage/srp?productType\u003dSRPE2E\u0026productSubtype\u003dTERMLIFE\u0026pageCode\u003dSRP_REVIEW_FORM\u0026apiCode",
    "customerHash": "fd368af3f2123d7462d396d35b387f0a",
    "createdAt": "2025-06-11 07:25:22.971000 UTC"
  },
  {
    "url": "/swt?swtUrl\u003dhttps%3A%2F%2Fhqa1.bigbasket.com%2Fsessionbridge%2F%3Fnext%3Dmember%2Forder-details%2Freturn-exchange%2F%3Ftcp_bb_gating%3D1%26show_bb_pseudo_door%3D1%26utm_source%3Dtcp%26utm_medium%3Dsuperapp%26source%3Dtcp%26isSwtRedirectionRequired%3Dtrue%26forcedSwtRedirection%3Dtrue%26order_id%3D1399426409%26p_order_id%3D1027900381%26entrycontextid%3D27\u0026programId\u003dbbgrsfab-0bfd-5c0e-7a7d-7bee045ee970\u0026isActionCompleted\u003dtrue",
    "customerHash": "69b0ecef200c9081d8d365156e8e648d",
    "createdAt": "2025-06-11 07:26:13.357000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/tsss/offers/tatamotors/power-of-12",
    "customerHash": "41c230886415978b90f46c953b15239e",
    "createdAt": "2025-06-11 07:26:18.048000 UTC"
  },
  {
    "url": "https://stg.skinn.in/",
    "customerHash": "",
    "createdAt": "2025-06-11 07:27:47.129000 UTC"
  },
  {
    "url": "https://preprod-pwa.croma.com/e-bosch-samsung-w-m-tl-10kg-woa106x0in-inx-5s/p/207799",
    "customerHash": "e08546c920f64af20d760a31f0e69d17",
    "createdAt": "2025-06-11 07:29:22.112000 UTC"
  },
  {
    "url": "https://luxpreprod2.tataunistore.com/",
    "customerHash": "7905424926730a933720436a27ceee33",
    "createdAt": "2025-06-11 07:30:29.756000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/home",
    "customerHash": "77b5970f785b4b2641aa4359fa186598",
    "createdAt": "2025-06-11 07:30:45.840000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/home",
    "customerHash": "77b5970f785b4b2641aa4359fa186598",
    "createdAt": "2025-06-11 07:30:46.383000 UTC"
  },
  {
    "url": "https://tsss-sit.tatadigital.com/tsss/lead-journey-details-dialog",
    "customerHash": "72223adc4e0debbd3dd9786bda9146e1",
    "createdAt": "2025-06-11 07:30:53.042000 UTC"
  },
  {
    "url": "https://stag.1mg.com/#",
    "customerHash": "8f98808e2e61721053713d5ba5ed0080",
    "createdAt": "2025-06-11 06:44:58.915000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/billpayment/landing-pwa",
    "customerHash": "f9fe3602dfcaa925de0aaf9fbecc9f3f",
    "createdAt": "2025-06-11 06:45:17.729000 UTC"
  },
  {
    "url": "https://eyeplus.newstore.co.in/my-account/orders",
    "customerHash": "",
    "createdAt": "2025-06-11 06:45:20.388000 UTC"
  },
  {
    "url": "http://localhost:3000/health-record/c5b8208d-004d-44a3-9a33-a06d3648387d/health-score",
    "customerHash": "e95098cce992d20c77b523d8df265757",
    "createdAt": "2025-06-11 06:45:20.580000 UTC"
  },
  {
    "url": "https://preprod-pwa.croma.com/checkout",
    "customerHash": "4e9ff813f9d198b2321a08837bfb61e7",
    "createdAt": "2025-06-11 06:45:21.796000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/billpayment/alertcrosscartitems?pageTitle\u003dbillpayhomescreen",
    "customerHash": "f9fe3602dfcaa925de0aaf9fbecc9f3f",
    "createdAt": "2025-06-11 06:45:21.885000 UTC"
  },
  {
    "url": "",
    "customerHash": "c65c2e9c9b3997633befc328404b2336",
    "createdAt": "2025-06-11 06:45:43.132000 UTC"
  },
  {
    "url": "https://author-tatapassenger-dev.adobecqms.net/content/tml/ev/in/en/service/service-feedback.html",
    "customerHash": "",
    "createdAt": "2025-06-11 06:45:59.589000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/travel/flights/setPaxInavalidDialog",
    "customerHash": "b55a0382a80392228276820fefad1c20",
    "createdAt": "2025-06-11 06:46:01.760000 UTC"
  },
  {
    "url": "http://localhost:3000/red-tape-black-walking-shoes/p-mp000000006312226",
    "customerHash": "e7fb619325d93352d37af6bfd3eaa71b",
    "createdAt": "2025-06-11 06:46:22.666000 UTC"
  },
  {
    "url": "/finance/insurance/health/postPayment",
    "customerHash": "12d359e3a830588b5f6bbcd78e6d5371",
    "createdAt": "2025-06-11 06:46:28.193000 UTC"
  },
  {
    "url": "http://localhost:3000/en-in/hotels/vivanta-ahmedabad/event-venues",
    "customerHash": "",
    "createdAt": "2025-06-11 06:46:44.022000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/travel/flights/confirmation?breadCrumbPath\u003deyJicmVhZGNydW1iTGlzdCI6WyIvdHJhdmVsL2hvbWUiXX0\u003d\u0026isCombineFlight\u003dfalse",
    "customerHash": "b55a0382a80392228276820fefad1c20",
    "createdAt": "2025-06-11 06:46:51.381000 UTC"
  },
  {
    "url": "https://preprod-pwa.croma.com/order-confirmation?status\u003dCHARGED\u0026status_id\u003d21\u0026order_id\u003dEC253033666048-11064611\u0026signature\u003d6ho3Ee3fxAKpf%2Ba%2FM9KPTLwYjTO7%2BtrtGio4qEbm%2FvA%3D\u0026signature_algorithm\u003dHMAC-SHA256",
    "customerHash": "4e9ff813f9d198b2321a08837bfb61e7",
    "createdAt": "2025-06-11 06:47:33.682000 UTC"
  },
  {
    "url": "/neumoney-category/home",
    "customerHash": "",
    "createdAt": "2025-06-11 06:47:36.906000 UTC"
  },
  {
    "url": "",
    "customerHash": "c7b61e7f0fc9621ba5ea6d9504c8fe8f",
    "createdAt": "2025-06-11 06:47:59.435000 UTC"
  },
  {
    "url": "https://hqa1.bigbasket.com/",
    "customerHash": "7b6151b41d857fe0d7b4fb10edbb4387",
    "createdAt": "2025-06-11 06:48:07.874000 UTC"
  },
  {
    "url": "http://localhost:3000/search/?q\u003dlipstick%3Arelevance%3AinStockFlag%3Atrue%3Abrand%3AMBH22A00002",
    "customerHash": "e7fb619325d93352d37af6bfd3eaa71b",
    "createdAt": "2025-06-11 06:48:34.904000 UTC"
  },
  {
    "url": "/hamburger-menu/logged-in/5_5",
    "customerHash": "2813fdbe950673d84081704a3e82925b",
    "createdAt": "2025-06-11 06:48:36.058000 UTC"
  },
  {
    "url": "https://luxpreprod2.tataunistore.com/",
    "customerHash": "39100b6c97a4cadb10203bea0c8872fd",
    "createdAt": "2025-06-11 06:48:43.347000 UTC"
  },
  {
    "url": "/auth/login",
    "customerHash": "",
    "createdAt": "2025-06-11 06:48:47.462000 UTC"
  },
  {
    "url": "/neumoney",
    "customerHash": "",
    "createdAt": "2025-06-11 06:49:03.458000 UTC"
  },
  {
    "url": "https://airindiaexpress-dev2.adobecqms.net/guest-information",
    "customerHash": "",
    "createdAt": "2025-06-11 06:49:17.544000 UTC"
  },
  {
    "url": "/finance/insurance/life/dynamicPage/srp?productType\u003dSRPE2E\u0026productSubtype\u003dTERMLIFE\u0026pageCode\u003dSRP_PAYMENT\u0026apiCode\u0026order_id\u003d5c4a8abf-f8fa-4a3a-9a96-1df18aef7795",
    "customerHash": "c7b61e7f0fc9621ba5ea6d9504c8fe8f",
    "createdAt": "2025-06-11 06:49:28.574000 UTC"
  },
  {
    "url": "/home",
    "customerHash": "",
    "createdAt": "2025-06-11 06:49:46.969000 UTC"
  },
  {
    "url": "/finance/insurance/life/dynamicPage/srp?productType\u003dSRPE2E\u0026productSubtype\u003dTERMLIFE\u0026pageCode\u003dSRP_MISMATCHED_KYC_MANUAL_FORM\u0026apiCode\u003dSRP_KYC_DETAILS_FOR_MANUAL_FORM",
    "customerHash": "c7b61e7f0fc9621ba5ea6d9504c8fe8f",
    "createdAt": "2025-06-11 06:50:06.049000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/home",
    "customerHash": "",
    "createdAt": "2025-06-11 06:50:15.025000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/hamburger-menu/anonymous/5_5",
    "customerHash": "",
    "createdAt": "2025-06-11 06:50:15.053000 UTC"
  },
  {
    "url": "/finance/insurance/health/ageSelection",
    "customerHash": "ded614be4d92f18df814b6cb2b2fcd44",
    "createdAt": "2025-06-11 06:50:56.669000 UTC"
  },
  {
    "url": "https://gateway-web-qa1v2.tajhotels.com/en-in/offers",
    "customerHash": "",
    "createdAt": "2025-06-11 06:50:56.845000 UTC"
  },
  {
    "url": "/home",
    "customerHash": "",
    "createdAt": "2025-06-11 06:51:09.675000 UTC"
  },
  {
    "url": "https://preprod1.tataunistore.com/nuon-by-westside-mid-blue-rocker-skinny-fit-jeans/p-mp000000000018601",
    "customerHash": "3be52f20d204bbf262df15320f21bef1",
    "createdAt": "2025-06-11 06:51:11.088000 UTC"
  },
  {
    "url": "http://localhost:3000/oxolloxo-brown-luxe-spaces-beach-dress/p-mp000000006101605",
    "customerHash": "e7fb619325d93352d37af6bfd3eaa71b",
    "createdAt": "2025-06-11 06:51:43.247000 UTC"
  },
  {
    "url": "/finance/insurance/my-plans-claims",
    "customerHash": "ded614be4d92f18df814b6cb2b2fcd44",
    "createdAt": "2025-06-11 06:51:44.290000 UTC"
  },
  {
    "url": "/finance/pl-marketplace/landing?utm_code\u003dgeneric",
    "customerHash": "",
    "createdAt": "2025-06-11 06:51:49.542000 UTC"
  },
  {
    "url": "/fs-slp/insurance",
    "customerHash": "",
    "createdAt": "2025-06-11 06:51:53.424000 UTC"
  },
  {
    "url": "http://localhost:3000/health-record/c5b8208d-004d-44a3-9a33-a06d3648387d/health-score",
    "customerHash": "e95098cce992d20c77b523d8df265757",
    "createdAt": "2025-06-11 06:52:03.143000 UTC"
  },
  {
    "url": "/hamburger-menu/logged-in/5_5",
    "customerHash": "83b664a91677624f9f6cdc037b80f56a",
    "createdAt": "2025-06-11 06:52:06.694000 UTC"
  },
  {
    "url": "https://luxpreprod2.tataunistore.com/search/?q\u003dbvlgari:relevance:category:LSH1:superBrand:SBD11A11124\u0026searchCategory\u003dLSH1",
    "customerHash": "39100b6c97a4cadb10203bea0c8872fd",
    "createdAt": "2025-06-11 06:52:20.313000 UTC"
  },
  {
    "url": "https://preprod1.tataunistore.com/checkout",
    "customerHash": "3be52f20d204bbf262df15320f21bef1",
    "createdAt": "2025-06-11 06:52:20.356000 UTC"
  },
  {
    "url": "https://dev1-pwa.croma.com/checkout",
    "customerHash": "ed53cea5198fc1214767d9f6228fa5fd",
    "createdAt": "2025-06-11 06:52:47.922000 UTC"
  },
  {
    "url": "https://preprod1.tataunistore.com/checkout/payment-method/cardPayment?value\u003d26749a34-24ce-411f-93be-4556199d5237\u0026status\u003dCHARGED\u0026status_id\u003d21\u0026order_id\u003d380698890\u0026signature\u003dgLYaQZTCulGddvFi1fltIEY1la1xfeTKAIwQI1tdZrs%3D\u0026signature_algorithm\u003dHMAC-SHA256",
    "customerHash": "3be52f20d204bbf262df15320f21bef1",
    "createdAt": "2025-06-11 06:53:03.590000 UTC"
  },
  {
    "url": "https://eyeplus.newstore.co.in/my-account/order-return/736",
    "customerHash": "2b2ef9d1f58bc67fa38825b8bdd53a68",
    "createdAt": "2025-06-11 06:53:10.474000 UTC"
  },
  {
    "url": "/finance/insurance/life/dynamicPage/srp?productType\u003dSRPE2E\u0026productSubtype\u003dTERMLIFE\u0026pageCode\u003dSRP_PDP\u0026apiCode\u003dPDP_LANDING",
    "customerHash": "fd368af3f2123d7462d396d35b387f0a",
    "createdAt": "2025-06-11 06:53:14.523000 UTC"
  },
  {
    "url": "https://sit.tataneu.com/my-neucoins-refresh",
    "customerHash": "e6a35d04e5013f18eec57fb03f23eb3d",
    "createdAt": "2025-06-11 06:53:28.562000 UTC"
  },
  {
    "url": "https://airindiaexpress-dev2.adobecqms.net/home",
    "customerHash": "",
    "createdAt": "2025-06-11 06:53:49.473000 UTC"
  },
  {
    "url": "https://stg.tanishq.co.in/cart?lang\u003den_IN",
    "customerHash": "e8bd0fdc25defec00e4aa4d8d39cc156",
    "createdAt": "2025-06-11 06:54:11.832000 UTC"
  },
  {
    "url": "http://localhost:3333/home",
    "customerHash": "",
    "createdAt": "2025-06-11 06:54:17.150000 UTC"
  },
  {
    "url": "http://localhost:3000/en-in/offers",
    "customerHash": "2a911b1bff6488aa12a5be263d29a179",
    "createdAt": "2025-06-11 06:54:43.610000 UTC"
  },
  {
    "url": "/auth/login",
    "customerHash": "",
    "createdAt": "2025-06-11 06:54:47.858000 UTC"
  },
  {
    "url": "https://hqa1.bigbasket.com/co/checkout/",
    "customerHash": "7b6151b41d857fe0d7b4fb10edbb4387",
    "createdAt": "2025-06-11 06:55:27.658000 UTC"
  },
  {
    "url": "http://localhost:3000/c-msh1311128101?page\u003d0\u0026pageSize\u003d20\u0026isTextSearch\u003dfalse\u0026isFilter\u003dfalse\u0026isPwa\u003dtrue\u0026channel\u003dmobile\u0026typeID\u003dall\u0026isMDE\u003dtrue\u0026isKeywordRedirect\u003dfalse\u0026isKeywordRedirectEnabled\u003dtrue\u0026visualFilter\u003d\u0026providePopular\u003dtrue\u0026currentStore\u003dfashion\u0026q\u003d:relevance:inStockFlag:true:category:MSH1311128101:colour:Maroon_800000",
    "customerHash": "e7fb619325d93352d37af6bfd3eaa71b",
    "createdAt": "2025-06-11 06:55:32.362000 UTC"
  },
  {
    "url": "/auth/login",
    "customerHash": "",
    "createdAt": "2025-06-11 06:55:33.563000 UTC"
  },
  {
    "url": "/swt?swtUrl\u003dhttps%3A%2F%2Fpreprod-pwa.croma.com%2Fgo%2520to%2520cart%3FNavigation_Enabled%3DFalse%26authRequired%3DFalse%26native_source%3Dtcp-android%26guid%3DAN_CR-2095811475bed6aaed19944d00a430f2698aae490f8720070387140087857110\u0026programId\u003d73eb6345-9cc9-4c37-a8e8-8620d6d32cf5",
    "customerHash": "",
    "createdAt": "2025-06-11 06:55:48.564000 UTC"
  },
  {
    "url": "https://airindiaexpress-dev2.adobecqms.net/guest-information?origin\u003dDEL\u0026destination\u003dGAU\u0026triptype\u003dOne%20Way\u0026arrivalTime\u003d09:40\u0026deartureTime\u003d07:20\u0026departureDate\u003d2025-06-27\u0026OneWayFlightCode\u003dIX%201191\u0026journeyKeyOneWay\u003dSVh_MTE5MX4gfn5ERUx_MDYvMjcvMjAyNSAwNzoyMH5HQVV_MDYvMjcvMjAyNSAwOTo0MH5_",
    "customerHash": "",
    "createdAt": "2025-06-11 06:55:51.212000 UTC"
  },
  {
    "url": "/electronics/cart",
    "customerHash": "",
    "createdAt": "2025-06-11 06:55:54.090000 UTC"
  },
  {
    "url": "/electronics/cart",
    "c_hash": ""
  }
]

with open("./visits.json", "w") as f:
    f.write(json.dumps(visits))