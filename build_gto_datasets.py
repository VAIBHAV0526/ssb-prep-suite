import json, os

out_dir = r'C:\Users\Singh\.gemini\antigravity\scratch\ssb-wat-simulator'

# Raw topics extracted from user's 7-page document
raw_topics = [
    # Page 1
    "Cyber warfare", "Investment banking", "Freedom of press", "New parliament building",
    "Criminalization of politics", "Importance of balanced Diet", "Anti conversion Law",
    "Agneepath scheme", "Swachh bharat cess", "NPA- Non performing assets", "Gatishakti",
    "Khelo india", "Blockchain", "Organic farming", "Non-Proliferation Treaty", "Civic duty",
    "Special economy zone", "Digital detox", "Debt trap policy of china", "Terror financing",
    "Asymmetric warfare", "Disaster Management", "India's Border issues", "Biased Journalism",
    "Importance of border roads & infrastructure", "Privatizations of PSUs", "Distance education",
    "Jal Jeevan Mission", "Child Abuse", "Swach Bharat mission", "Digital India", "My favorite sports",
    "Crypto currency", "Election commission of India",
    # Page 2
    "National bird of india", "Mangalyan mission", "Unemployment", "India in 2050", "Voting rights",
    "E-money", "Youth in national politics", "Genetically modified crops", "Regional parties",
    "Space technology", "Mercy killing", "Small states are better for governance", "Clean energy",
    "Radicalization", "Monsoon in India", "Dynasty politics", "Land mafia", "Solar energy",
    "India-A new global manufacturing Hub", "Plebiscite", "Blood donation", "War crimes",
    "Digital media vs print media", "China-A rival of India", "ASEAN", "Gaganyan", "Startups in india",
    "Healthcare industry", "Transport system in India", "Online game addiction", "Rain water harvesting",
    "Gender inequality", "Nationalism", "Inflation", "Nuclear Suppliers group", "UNSC",
    "Artificial Intelligence", "Genetic Cloning", "IPL",
    # Page 3
    "Tidal Energy", "E-learning", "Cross border terrorism", "Implications of social media",
    "Crime against women", "Electric vehicles", "Betting in sports", "Fossil fuels", "South china sea",
    "Fitness industry", "International space station", "One nation one election", "Women protection Bill",
    "Free education for all", "Judiciary in India", "Border road organization", "Bipin Rawat",
    "Driverless cars", "Street food", "Ayurveda vs modern medicine", "India-srilanka relations",
    "Bharatmala project", "Indo-Israel Relations", "Indo- Afghanistan Relations", "Galwan Valley Conflict",
    "Indo US Relations", "Naxalism", "G8 Nations", "Indian missile programme", "Role of discipline in life",
    "Brain drain", "Women empowerment", "Rivers in India", "Problem that farmers are facing in India",
    "Farming Reforms in India", "Indo-Russia Relationship", "India – Australia Relationship",
    "QUAD", "One Belt One Road Initiative",
    # Page 4
    "Citizenship amendment Act 2019", "Removal of Art 370 – A Road ahead for Future India", "UPSC",
    "Micro Finance", "Books vs E-books", "Role of youth in Nation Building", "Mobile Phones",
    "New World order", "Indo-france relations", "Indo-UK relations", "Students Union", "IT Industry",
    "Your Favorite Day", "Smart Card", "E-Commerce", "Cyber Crime", "Sports in India",
    "Role of Opposition in Indian Politics", "BPO vs KPO", "Why Youth Hesitate to Join Defense Forces",
    "Peaceful use of NuclearEnergy", "Globalization", "India's Agricultural Problem", "My Favorite Actress",
    "India and USA in Changing World", "Child Labor", "USA -A Policeman of Unipolar World",
    "Education is a Modern Day Industry", "Religion-A Secular View in Indian Society",
    "Indian Society-Turning to Western Way of Life", "Infrastructure of India",
    "Disasters in Coastal Areas", "Tsunami",
    # Page 5
    "Status of Women in India", "Govt Schools vs Public School", "Insurgency-A Phenomenon Needs Understanding",
    "E Governance", "Health Tourism", "National Anthem", "G 20", "Secularism", "Ambition in Life",
    "Financial Education", "Internet", "Rattan Tata-A Business Personality", "Politicians in India-Root Cause of Problems",
    "Indian Democracy", "Democracy v/s Dictatorship", "Aviation Industry in Developing India",
    "Bribery-A Cancer of Indian Society", "Constitution of India", "Mutual Funds", "Higher Education in India",
    "Life Insurance Industry in India", "Indian Cinema Industry (Bollywood)", "Internet-A Boon or Curse",
    "Political Leadership in India", "Girl Child in Indian Society", "Center -State Relations",
    "Kashmir Issue- A Mistake by Pt. Jawahar Lal Nehru", "Sarkaria Commission", "NSG", "Generation Gap",
    "Call Center", "Population Problem", "Shah Commission", "Ragging in Colleges/Universities",
    # Page 6
    "Distance Learning", "Entry of Foreign Universities in India", "Pollution", "Cricket vs Other Games in India",
    "Our Fundamental Rights", "Siachen Glacier", "Value of Computer Education", "Alternate Sources of Energy",
    "Reverse Brain drain", "Professional Education in India", "Homeopathy An Established Medical Science",
    "Yoga- A Gift to Present World by India", "Corrupt Politicians -An Issue Requires Attention",
    "Traffic Problem", "Energy Industry in Our Country", "Family Planning", "Malnutrition",
    "Medical infrastructure in India", "Nuclear Families", "Farmers' suicide", "Poverty in India",
    "Green House Effect", "Co-ed Education", "Terrorist Problem in Kashmir", "Terrorism in North Eastern India",
    "Doping in Sports", "Division Of States in India", "Role of NGO", "My Hobby", "Role of Media",
    "Global Warming", "India as Superpower", "Discoveries that Changed the World", "Indo Pak Relations",
    "India's Nuclear policy", "Joint Family Vs Nuclear Family",
    # Page 7
    "Wildlife Protection", "Eye Donation", "Nuclear Disarmament", "India's Foreign Trade",
    "Technology in Agriculture", "United We Stand, Divided We Fall", "Can India Become Self Sufficient in Energy Resources",
    "Indian Reservation Policy", "Missile Programme of India", "LGBTQ Rights", "ISRO", "Disinvestment of PSUs",
    "Nano Technology", "National Highway Authority of India", "Climate Change Effect on India",
    "Gilgit-Baltistan Dispute - India and Pakistan", "Rising Oil Prices - Reasons and Impact",
    "Dholavira - UNESCO World Heritage Site", "Drone Attacks", "Fuel Price and Inflation",
    "Gender Equality in the workplace", "Armed Forces role in Curbing Covid", "Cyber Threat",
    "Forest Rights and Forest Conservation", "Containing the Rural COVID-19 Spread", "India's Africa Policy",
    "Single Use Plastics", "India and Food Security", "Relevance of MSP system in agriculture in modern times",
    "Reservation in Jobs", "Overcrowded Jails", "India's Taliban Challenge", "Army for Anti Naxal Operations",
    "Caste Census", "Childhood Cancer", "Fuel Price Influence on Food"
]

# Deduplicate preserving order
seen = set()
unique_topics = []
for t in raw_topics:
    clean = t.strip()
    norm = clean.lower()
    if norm not in seen and len(norm) > 2:
        seen.add(norm)
        unique_topics.append(clean)

print(f"Total Unique Lecturette Topics: {len(unique_topics)}")

# Define categorization rules for the 4 official DIPR Tiers:
# Tier 1: International Relations, Defense, Geopolitics, Security, Treaties
# Tier 2: National Strategy, Economy, Governance, Policy, Institutions
# Tier 3: Social, Science & Tech, Environment, Education, Health
# Tier 4: Basic, Personal, Sports, General Culture, Hobbies

tier1_keywords = ['war', 'defense', 'defence', 'military', 'army', 'border', 'galwan', 'pak', 'china',
                  'russia', 'us relations', 'indo-', 'quad', 'treaty', 'nsg', 'unsc', 'nuclear', 'missile',
                  'siachen', 'terror', 'insurgency', 'naxal', 'bipin rawat', 'asean', 'g8', 'g20',
                  'south china sea', 'belt one road', 'drone', 'disarmament', 'kashmir', 'gilgit',
                  'taliban', 'asymmetric', 'cyber warfare', 'weapons']

tier4_keywords = ['my favorite', 'my hobby', 'sports', 'cricket', 'ipl', 'yoga', 'street food', 'diet',
                  'bird', 'day', 'ambition', 'discipline', 'books vs', 'national anthem', 'actress',
                  'united we stand', 'eye donation', 'hobbies', 'cinema', 'bollywood']

tier2_keywords = ['parliament', 'politics', 'election', 'constitution', 'judiciary', 'upsc', 'art 370',
                  'caa', 'citizenship', 'sarkaria', 'commission', 'gatishakti', 'bharatmala', 'npa',
                  'psu', 'economy', 'economic', 'banking', 'mutual fund', 'insurance', 'inflation',
                  'bpo', 'manufacturing', 'infrastructure', 'one nation', 'democra', 'states', 'governance',
                  'superpower', 'foreign trade', 'nhai', 'msp', 'reservation', 'jail', 'census']

tier1_list = []
tier2_list = []
tier3_list = []
tier4_list = []

for t in unique_topics:
    tl = t.lower()
    if any(k in tl for k in tier4_keywords):
        tier4_list.append(t)
    elif any(k in tl for k in tier1_keywords):
        tier1_list.append(t)
    elif any(k in tl for k in tier2_keywords):
        tier2_list.append(t)
    else:
        tier3_list.append(t)

print(f"Tiers Count -> T1 (Geopolitics/Defense): {len(tier1_list)}, T2 (National/Economy): {len(tier2_list)}, T3 (Social/Tech/Env): {len(tier3_list)}, T4 (Basic/Sports): {len(tier4_list)}")

# Generate balanced 4-topic DIPR Cue Cards
# Each card has: 1 from Tier 1, 1 from Tier 2, 1 from Tier 3, 1 from Tier 4
num_cards = min(len(tier1_list), len(tier2_list), len(tier3_list), len(tier4_list))
# To ensure at least 40-50 cards, we can cycle through lists if needed
target_cards = 50
cue_cards = []
for i in range(target_cards):
    t1 = tier1_list[i % len(tier1_list)]
    t2 = tier2_list[i % len(tier2_list)]
    t3 = tier3_list[i % len(tier3_list)]
    t4 = tier4_list[i % len(tier4_list)]
    cue_cards.append({
        "card_id": i + 1,
        "title": f"DIPR Card #{i + 1}",
        "topics": [
            { "tier": 1, "tier_name": "International Relations & Defense", "topic": t1 },
            { "tier": 2, "tier_name": "National Strategy & Governance", "topic": t2 },
            { "tier": 3, "tier_name": "Social, Science & Environment", "topic": t3 },
            { "tier": 4, "tier_name": "Basic, Sports & Culture", "topic": t4 }
        ]
    })

lecturette_data = {
    "total_topics": len(unique_topics),
    "all_topics": unique_topics,
    "tiers": {
        "tier1": tier1_list,
        "tier2": tier2_list,
        "tier3": tier3_list,
        "tier4": tier4_list
    },
    "cards": cue_cards
}

with open(os.path.join(out_dir, 'lecturette_topics.json'), 'w', encoding='utf-8') as f:
    json.dump(lecturette_data, f, indent=2)

print("Saved lecturette_topics.json successfully!")

# Build 25+ Comprehensive GD Topics with 3 Leads and Syndicate Dialogues
gd_scenarios = [
    {
        "id": 1,
        "title": "Modernization of Indian Armed Forces: Priority Areas",
        "category": "Defense & Security",
        "context": "Faced with evolving two-front security challenges and gray-zone hybrid warfare, how should India allocate its modernization capital?",
        "leads": [
            "1. Indigenous R&D and Make in India (Atmanirbharta)",
            "2. Cyber, Space, and AI-enabled Electronic Warfare",
            "3. Joint Theater Commands & Tri-Services Integration"
        ],
        "peer_dialogues": [
            { "speaker": "Chest 2", "time_sec": 15, "lead": 1, "text": "Gentlemen, recent global conflicts demonstrate that foreign supply dependencies during wartime can choke frontline operational readiness. Indigenous manufacturing must be our number one priority." },
            { "speaker": "Chest 4", "time_sec": 50, "lead": 2, "text": "I see your point, but modern conflicts are decided before ground troops engage. A single coordinated cyber assault on power grids and satellite communications can neutralize our command networks." },
            { "speaker": "Chest 7", "time_sec": 95, "lead": 1, "text": "Adding to Chest 2's point, our private defense startups are already delivering loitering munitions and indigenous radar systems at one-third the cost of imports." },
            { "speaker": "Chest 9", "time_sec": 140, "lead": 3, "text": "Friends, while platforms and technology are vital, without Joint Theater Commands, our tri-services will continue operating in individual silos. Operational synergy is the true force multiplier." },
            { "speaker": "Chest 2", "time_sec": 210, "lead": 2, "text": "Indeed, China's Strategic Support Force combines space, cyber, and electronic warfare. India needs dedicated cyber defense commands with private tech partnership." },
            { "speaker": "Chest 7", "time_sec": 280, "lead": 3, "text": "Let us also evaluate budgetary constraints. Indigenous production saves foreign exchange, which can then be funneled into joint command data links." }
        ]
    },
    {
        "id": 2,
        "title": "India's Strategic Posture in the Indo-Pacific: QUAD vs Non-Alignment",
        "category": "Geopolitics & Foreign Affairs",
        "context": "As maritime trade corridors and the South China Sea face increasing militarization, how should India navigate strategic partnerships?",
        "leads": [
            "1. Deepening Military Interoperability with QUAD (US, Japan, Australia)",
            "2. Preserving Strategic Autonomy & Diversified Multipolarity",
            "3. Expanding Naval Power Projection across the Indian Ocean Region (IOR)"
        ],
        "peer_dialogues": [
            { "speaker": "Chest 2", "time_sec": 15, "lead": 1, "text": "Friends, the Malacca Strait is our economic lifeline. Enhancing Malabar naval drills and maritime domain awareness through QUAD guarantees regional deterrence." },
            { "speaker": "Chest 4", "time_sec": 55, "lead": 2, "text": "However, we must remember that QUAD is not a treaty alliance like NATO. If a continental land border conflict flares up, India stands alone. Strategic autonomy must remain paramount." },
            { "speaker": "Chest 9", "time_sec": 105, "lead": 3, "text": "Gentlemen, rather than relying on external pacts, our primary objective must be building a 200-ship navy with indigenous aircraft carriers and nuclear attack submarines in the IOR." },
            { "speaker": "Chest 7", "time_sec": 160, "lead": 1, "text": "I agree with Chest 9 on indigenous strength, but logistics exchange agreements like LEMOA and COMCASA give our fleet access to naval ports from Bahrain to Guam." },
            { "speaker": "Chest 4", "time_sec": 230, "lead": 2, "text": "We must also consider our defense imports from Russia. Over-tilting toward Western security frameworks could alienate long-standing energy and defense partnerships." }
        ]
    },
    {
        "id": 3,
        "title": "Agnipath Scheme: Transforming the Military Demographic Profile",
        "category": "Defense & Human Resource",
        "context": "The recruitment model for soldiers, sailors, and airmen aims to create a youthful, tech-savvy fighting force while optimizing pension expenditure.",
        "leads": [
            "1. Operational Fitness & Tech-Savvy Profile of Youth",
            "2. Retention Ratio and Retention of Specialized Combat Skills",
            "3. Re-employment and Corporate Integration of Demobilized Agniveers"
        ],
        "peer_dialogues": [
            { "speaker": "Chest 2", "time_sec": 15, "lead": 1, "text": "Gentlemen, the average age of Indian soldiers was 32 years compared to 26 globally. Agnipath lowers our combat age profile, bringing superior physical stamina to high-altitude warfare." },
            { "speaker": "Chest 4", "time_sec": 55, "lead": 2, "text": "While stamina is important, 4 years is too short to master modern missile batteries, radar systems, and armored crew coordination. We risk losing technical institutional memory." },
            { "speaker": "Chest 7", "time_sec": 110, "lead": 3, "text": "On post-service rehabilitation, paramilitary forces and state police quotas are already reserving 10% vacancies. A disciplined, trained youth entering the civilian workforce benefits the nation." },
            { "speaker": "Chest 9", "time_sec": 170, "lead": 2, "text": "A middle ground would be raising the permanent retention percentage from 25% to 50% for high-skill technical cadres like aviation technicians and sonar operators." },
            { "speaker": "Chest 2", "time_sec": 240, "lead": 1, "text": "Let us not forget that saving nearly 50% of revenue budgets on pensions allows the military to divert thousands of crores toward capital weapon procurements." }
        ]
    },
    {
        "id": 4,
        "title": "One Nation, One Election: Feasibility and Democratic Impact",
        "category": "National Governance & Polity",
        "context": "Simultaneous elections for Lok Sabha and State Legislative Assemblies are proposed to curb governance paralysis and recurring public expenditure.",
        "leads": [
            "1. Reducing Continuous Election Expenditure and Governance Paralysis",
            "2. Constitutional Feasibility and Impact on Federal Autonomy",
            "3. Regional Priorities versus National Narrative Dominance"
        ],
        "peer_dialogues": [
            { "speaker": "Chest 4", "time_sec": 20, "lead": 1, "text": "Friends, India is in a perpetual state of election mode. The Model Code of Conduct halts developmental decisions for 4 to 5 months every single year." },
            { "speaker": "Chest 7", "time_sec": 65, "lead": 2, "text": "While economic savings are valid, our Constitution establishes a federal union. Dissolving or truncating elected state assembly tenures artificially undermines voter mandate." },
            { "speaker": "Chest 2", "time_sec": 120, "lead": 3, "text": "Regional concerns are crucial. In simultaneous polls, national security and defense issues often overshadow local water disputes, farmer distress, and state civic deficits." },
            { "speaker": "Chest 9", "time_sec": 180, "lead": 1, "text": "The Kovind Committee's two-phase framework proposes harmonizing municipal elections separately, which balances federalism while cutting down deployment of security forces." }
        ]
    },
    {
        "id": 5,
        "title": "Artificial Intelligence & Automation: Job Destroyer or Productivity Revolution",
        "category": "Economy & Technology",
        "context": "Rapid proliferation of generative AI and robotic process automation is restructuring India's IT services and white-collar employment landscape.",
        "leads": [
            "1. Disruption in Routine BPO and Entry-Level Software Engineering",
            "2. Creation of High-Value Technical Roles and Enterprise Productivity",
            "3. National Reskilling Initiatives & Ethical AI Regulation"
        ],
        "peer_dialogues": [
            { "speaker": "Chest 2", "time_sec": 15, "lead": 1, "text": "Gentlemen, India's IT industry employs over 5 million people, largely in maintenance and testing. Code-generating AI models will drastically compress entry-level hiring." },
            { "speaker": "Chest 9", "time_sec": 60, "lead": 2, "text": "Historically, technological shifts—from computers in the 1990s to ATM machines—initially sparked fears of job loss, but ultimately expanded economic output and created new job sectors." },
            { "speaker": "Chest 4", "time_sec": 115, "lead": 3, "text": "The transition will not be automatic. We need urgent curriculum overhauls in Tier-2 and Tier-3 engineering colleges to focus on prompt engineering, AI safety, and data governance." },
            { "speaker": "Chest 7", "time_sec": 175, "lead": 1, "text": "In agriculture and healthcare, AI diagnostics and crop monitoring can revolutionize grassroots rural productivity if deployed responsibly." }
        ]
    },
    {
        "id": 6,
        "title": "Uniform Civil Code (UCC): Gender Justice vs Cultural Diversity",
        "category": "Social & Constitutional Affairs",
        "context": "Article 44 of the Directive Principles envisions a common code for marriage, divorce, inheritance, and succession across all citizens.",
        "leads": [
            "1. Gender Justice and Equal Rights for Women across Personal Laws",
            "2. Protection of Tribal Customs and Pluralistic Traditions",
            "3. Incremental Law Commission Reforms vs Sweeping Legislation"
        ],
        "peer_dialogues": [
            { "speaker": "Chest 7", "time_sec": 15, "lead": 1, "text": "Friends, the core foundation of UCC must be viewed through gender justice. Every Indian woman, irrespective of faith, deserves equal inheritance and alimony protections." },
            { "speaker": "Chest 4", "time_sec": 65, "lead": 2, "text": "We must also recognize that tribal communities in Nagaland, Meghalaya, and Jharkhand have customary land and family laws protected under Article 371." },
            { "speaker": "Chest 2", "time_sec": 120, "lead": 3, "text": "Uttarakhand's model exempted scheduled tribes while standardizing marriage registration and live-in relationships. A phased, consensus-based state adoption is pragmatic." }
        ]
    },
    {
        "id": 7,
        "title": "Space Weaponization and India's Strategic Anti-Satellite Capabilities",
        "category": "Defense & Security",
        "context": "With low Earth orbit satellites directing military communications and GPS targeting, outer space is emerging as the fourth domain of warfare.",
        "leads": [
            "1. Mission Shakti & Kinetic vs Non-Kinetic ASAT Deterrence",
            "2. Commercial Space Megaconstellations and Space Debris Management",
            "3. Expanding Defence Space Agency (DSA) and Tri-Service Operations"
        ],
        "peer_dialogues": [
            { "speaker": "Chest 2", "time_sec": 20, "lead": 1, "text": "Mission Shakti demonstrated India's kinetic kill capability. However, modern space threats involve electronic jamming and cyber blinding of satellites without space debris." },
            { "speaker": "Chest 9", "time_sec": 70, "lead": 2, "text": "Space debris poses an existential risk to all nations. Kinetic ASAT strikes create thousands of fragments that can damage international satellites. Laser dazzlers are the future." },
            { "speaker": "Chest 4", "time_sec": 130, "lead": 3, "text": "Our Defence Space Agency must integrate NavIC civilian navigation with encrypted military bands to ensure precision missile guidance in denied electronic warfare zones." }
        ]
    },
    {
        "id": 8,
        "title": "Internal Security Challenges: Eradication of Left-Wing Extremism (Naxalism)",
        "category": "National Security",
        "context": "Security forces have drastically compressed the Red Corridor, but remote pockets in Bastar and Dandakaranya continue to demand sustained operational strategy.",
        "leads": [
            "1. Coordinated Security Operations and Forward Operating Bases (FOBs)",
            "2. Road Infrastructure, Telecom, and Tribal Land Rights",
            "3. Surrender & Rehabilitation Policies and Local Intelligence Networks"
        ],
        "peer_dialogues": [
            { "speaker": "Chest 4", "time_sec": 15, "lead": 1, "text": "Gentlemen, setting up Forward Operating Bases in interior forests has denied safe havens to naxal commanders and enabled security forces to dominate core insurgent redoubts." },
            { "speaker": "Chest 7", "time_sec": 65, "lead": 2, "text": "Security force presence alone will not eliminate extremism permanently. Road connectivity, primary health centers, and fair market prices for minor forest produce win tribal trust." },
            { "speaker": "Chest 2", "time_sec": 125, "lead": 3, "text": "Local tribal youth recruited into specialized police battalions like Bastar Fighters provide indigenous terrain intelligence that out-of-state forces cannot match." }
        ]
    }
]

with open(os.path.join(out_dir, 'gd_topics.json'), 'w', encoding='utf-8') as f:
    json.dump(gd_scenarios, f, indent=2)

print("Saved gd_topics.json successfully!")
