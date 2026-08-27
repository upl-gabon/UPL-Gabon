/**
 * UPL — configuration centrale du site
 * Modifier ICI pour contacts, feature flags, écoles futures.
 * Une IA ou un humain doit lire ce fichier en premier.
 */
window.UPL = window.UPL || {};

window.UPL.config = {
  institution: {
    name: "Université Privée de Libreville",
    short: "UPL",
    slogan: "Excellence · Innovation · Leadership",
    tagline: "Établissement privé d'enseignement supérieur — Libreville, Gabon",
    city: "Libreville",
    country: "Gabon",
    address: "Sablière, en face de la Résidence de l'Ambassade d'Arabie Saoudite — Libreville",
    foundedActivity: 2022,
    president: "Serge Patrick MINANG",
  },

  /* Charte (doit rester alignée avec assets/css/main.css) */
  brand: {
    bleu: "#0B2A5B",
    or: "#C9A227",
    blanc: "#FFFFFF",
  },

  contact: {
    email: "contact@upl-gabon.com",
    /* Lignes institution UPL */
    phonesUpl: [
      { label: "UPL", display: "+241 02 62 19 78", tel: "+24102621978" },
      { label: "UPL", display: "+241 07 35 95 72", tel: "+24107359572" },
    ],
    /* Président / épouse — questions UPL */
    phonesDirection: [
      { label: "Présidence / secrétariat", display: "+241 05 01 56 20", tel: "+24105015620" },
    ],
    /**
     * Calvin Blanchard MINANG — aide technique été 2026 UNIQUEMENT.
     * Ne pas afficher comme permanent sur le site grand public.
     * Urgence projet digital seulement.
     */
    calvinEmergency: {
      name: "Calvin Blanchard MINANG",
      role: "Appui digital (été 2026 — urgence only)",
      phone: "+33 7 52 97 58 09",
      tel: "+33752975809",
      email: "blanchardminang00@gmail.com",
      public: false,
    },
  },

  /**
   * Programmes.
   * status: "open" = affiché comme offre | "project" = pas sur le site public | "partner" = futur
   * Architecture multi-université : grouper par schoolId plus tard.
   */
  programmes: [
    {
      id: "licence-1",
      schoolId: "upl-facultes",
      title: "Licence 1",
      status: "open",
      tuition: "1 000 000 FCFA (50 premières inscriptions) / 1 200 000 FCFA",
      tuitionNote: "Frais d'inscription : 200 000 / 300 000 FCFA exigibles au dépôt du dossier — solde en 6 tranches",
    },
    {
      id: "master-1",
      schoolId: "upl-facultes",
      title: "Master 1",
      status: "open",
      tuition: "1 500 000 FCFA",
    },
    {
      id: "master-2",
      schoolId: "upl-facultes",
      title: "Master 2",
      status: "open",
      tuition: "2 000 000 FCFA",
    },
    {
      id: "cpge",
      schoolId: "upl-cpge",
      title: "Classes préparatoires aux Grandes Écoles (CPGE)",
      status: "open",
      tuition: "2 200 000 FCFA",
    },
    {
      id: "exec-mba",
      schoolId: "upl-executive",
      title: "Executive MBA",
      status: "open",
      audience: "Cadres et dirigeants en activité",
      partner: "Université de Douala",
      tuition: "4 000 000 FCFA",
      tuitionNote: "Droit de scolarité — promotion type",
      since: 2022,
      approxAlumni: 80,
      promoSize: 20,
    },
    {
      id: "dba",
      schoolId: "upl-facultes",
      title: "DBA",
      status: "open",
      tuition: "Sur dossier",
    },
  ],

  /**
   * Écoles / composantes — structure prête à grossir (multi-université).
   * Ne pas inventer d'offres : status "active" seulement si vrai.
   */
  schools: [
    {
      id: "upl-facultes",
      name: "Facultés UPL — 5 pôles (Gouvernance & Management · Économie Numérique & IA · Économie Bleue & Gestion Portuaire · Droit & Sciences Politiques · Assurance Maladie & Sécurité Sociale)",
      status: "active",
      blurb: "Formations diplômantes 2026-2027 (Licence, Master, DBA).",
    },
    {
      id: "upl-cpge",
      name: "Classes préparatoires aux Grandes Écoles (CPGE)",
      status: "active",
      blurb: "Préparation intensive aux concours des grandes écoles.",
    },
    {
      id: "upl-executive",
      name: "École executive",
      status: "active",
      blurb: "Formation de cadres et dirigeants — Executive MBA.",
    },
    /* Exemples futurs (status planned = non affiché en offre) :
    { id: "upl-ing", name: "Pôle ingénierie", status: "planned", blurb: "…" },
    { id: "upl-eco", name: "Pôle économie & management", status: "planned", blurb: "…" },
    */
  ],

  features: {
    showPartnershipsPage: false,
    showMultiFilieres: false,
    showMobileMoneyCheckout: false,
    showLibrary: false,
    showPresidentDashboard: false,
  },

  social: {
    /* Remplir quand les comptes officiels UPL sont créés (2 admins UPL) */
    facebook: "",
    instagram: "",
    linkedin: "",
    youtube: "https://www.youtube.com/@UPL",
  },

  media: [
    {
      title: "Interview Executive MBA",
      url: "https://youtu.be/FAKHfv8nN7I",
      thumb: "https://i.ytimg.com/vi/FAKHfv8nN7I/hqdefault.jpg",
      source: "Télévision Régionale",
    },
    {
      title: "Présentation institutionnelle",
      url: "https://youtu.be/jh_iCTJuLKA",
      thumb: "https://i.ytimg.com/vi/jh_iCTJuLKA/hqdefault.jpg",
      source: "Télévision Régionale",
    },
  ],

  /* Rentrée académique — laisser date vide tant qu'elle n'est pas confirmée par l'école.
     Format : "2026-10-05" (AAAA-MM-JJ). Tant que vide, le compte à rebours reste caché. */
  rentree: {
    date: "",
    label: "Rentrée académique",
    labelEn: "Academic year opening",
  },

  /* Situations pratiques — alternent avec les citations sur l'accueil.
     Paiement : justification de paiement + confirmation UPL indispensables (docs d'inscription). */
  paymentNotices: [
    {
      text: "Scolarité payable en tranches — l'échéancier est remis par le secrétariat à l'inscription.",
      source: "Modalités de paiement",
      textEn: "Tuition is payable in instalments — the schedule is handed over by the Secretariat upon enrolment.",
      sourceEn: "Payment terms",
    },
    {
      text: "Règlement par Airtel Money : conservez votre justificatif de paiement — la confirmation de l'UPL est indispensable.",
      source: "Paiement & inscription",
      textEn: "Pay via Airtel Money: keep your payment receipt — the UPL confirmation is mandatory.",
      sourceEn: "Payment & enrolment",
    },
    {
      text: "Après chaque versement, un reçu UPL vous est délivré : joignez-le à vos documents d'inscription.",
      source: "Justificatifs",
      textEn: "After each instalment you receive a UPL receipt: attach it to your enrolment documents.",
      sourceEn: "Supporting documents",
    },
  ],

  /* Défilement continu « À la une » : communiqués + infos pratiques. */
  tickerExtra: [
    { fr: "Inscriptions 2026-2027 ouvertes · Licence · Master · CPGE · MBA · DBA", en: "Admissions 2026-2027 open · Bachelor's · Master's · CPGE · MBA · DBA" },
    { fr: "Cours du soir 17h–21h · Sablière, Libreville", en: "Evening classes 5–9 pm · Sablière, Libreville" },
    { fr: "Scolarité payable en tranches · reçu + confirmation UPL", en: "Tuition payable in instalments · receipt + UPL confirmation" },
    { fr: "Inscriptions : contact@upl-gabon.com", en: "Admissions: contact@upl-gabon.com" },
  ],

  /* Citations de management — rotation aléatoire côté accueil.
     Choisir des citations sourcées (attribution fiable). */
  quotes: [
    {
      text: "Le management consiste à faire les choses correctement ; le leadership, à faire les bonnes choses.",
      author: "Peter Drucker",
      textEn: "Management is doing things right; leadership is doing the right things.",
    },
    {
      text: "Les plans ne sont que de bonnes intentions tant qu'ils ne se transforment pas immédiatement en travail.",
      author: "Peter Drucker",
      textEn: "Plans are only good intentions unless they immediately degenerate into hard work.",
    },
    {
      text: "La meilleure façon de prédire l'avenir, c'est de le créer.",
      author: "Peter Drucker",
      textEn: "The best way to predict the future is to create it.",
    },
    {
      text: "Quiconque cesse d'apprendre vieillit — qu'il ait vingt ou quatre-vingts ans.",
      author: "Henry Ford",
      textEn: "Anyone who stops learning is old, whether at twenty or eighty.",
    },
    {
      text: "L'éducation est l'arme la plus puissante qu'on puisse utiliser pour changer le monde.",
      author: "Nelson Mandela",
      textEn: "Education is the most powerful weapon which you can use to change the world.",
    },
    {
      text: "Un budget, c'est dire à son argent où aller, au lieu de se demander où il est passé.",
      author: "John C. Maxwell",
      textEn: "A budget is telling your money where to go instead of wondering where it went.",
    },
  ],

  /* Communiqués / actualités de l'école — mis à jour ICI (le plus récent en premier).
     Utiliser des faits réels ; date au mois, pas de date inventée. */
  news: [
    {
      tag: "Communiqué", tagEn: "Announcement",
      date: "Août 2026", dateEn: "August 2026",
      title: "Inscriptions ouvertes — rentrée 2026-2027",
      titleEn: "Admissions open — 2026-2027 academic year",
      text: "Licence, Master, CPGE, Executive MBA et DBA. Dossiers à déposer dès maintenant auprès du service des admissions — places limitées.",
      textEn: "Bachelor's, Master's, CPGE, Executive MBA and DBA. Apply now with the Admissions office — limited places.",
    },
    {
      tag: "Communiqué", tagEn: "Announcement",
      date: "Août 2026", dateEn: "August 2026",
      title: "Inscriptions ouvertes — Executive MBA",
      titleEn: "Admissions open — Executive MBA",
      text: "Constitution du dossier : CV, parcours, diplômes — par e-mail (objet « Candidature MBA ») ou dépôt au secrétariat, Sablière. Scolarité payable en tranches.",
      textEn: "Prepare your file (CV, background, diplomas) — by e-mail (subject « MBA Application ») or at the Secretariat, Sablière. Tuition is payable in instalments.",
    },
    {
      tag: "Vie de l'école", tagEn: "School life",
      date: "", dateEn: "",
      title: "Les cours du soir se poursuivent à la Sablière",
      titleEn: "Evening classes continue in Sablière",
      text: "Séances de 17h00 à 21h00, compatibles avec l'activité professionnelle des auditeurs. Emploi du temps remis au début de chaque module.",
      textEn: "Sessions run from 5:00 pm to 9:00 pm, compatible with the auditors' professional activity. The timetable is handed out at the start of each module.",
    },
    {
      tag: "Inscription", tagEn: "Admissions",
      date: "", dateEn: "",
      title: "Paiement : justificatif et confirmation UPL indispensables",
      titleEn: "Payment: proof of payment and UPL confirmation are mandatory",
      text: "Règlement des tranches par Airtel Money ou au secrétariat. Conservez votre justificatif de paiement : la confirmation de l'UPL complète votre dossier d'inscription.",
      textEn: "Instalments are settled via Airtel Money or at the Secretariat. Keep your payment receipt: the UPL confirmation completes your enrolment file.",
    },
    {
      tag: "Multimédia", tagEn: "Media",
      date: "", dateEn: "",
      title: "L'UPL en vidéo",
      titleEn: "UPL on video",
      text: "Présentation institutionnelle à la télévision (lecture automatique sur l'accueil) et interview sur l'Executive MBA — page MBA, section « Le MBA en images ».",
      textEn: "The televised institutional presentation (autoplay on the homepage) and the Executive MBA interview — MBA page, section « The MBA in pictures ».",
    },
  ],

  deploy: {
    domain: "upl-gabon.com",
    emailProvider: "PrivateEmail / Namecheap",
    preferredHost: "GitHub Pages",
    keepNetlifyUntilFinal: true,
  },
};
