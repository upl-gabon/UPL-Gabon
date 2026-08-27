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
  ],

  /**
   * Écoles / composantes — structure prête à grossir (multi-université).
   * Ne pas inventer d'offres : status "active" seulement si vrai.
   */
  schools: [
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
  },

  /* Situations pratiques — alternent avec les citations sur l'accueil.
     Paiement : justification de paiement + confirmation UPL indispensables (docs d'inscription). */
  paymentNotices: [
    {
      text: "Scolarité payable en tranches — l'échéancier est remis par le secrétariat à l'inscription.",
      source: "Modalités de paiement",
    },
    {
      text: "Règlement par Airtel Money : conservez votre justificatif de paiement — la confirmation de l'UPL est indispensable.",
      source: "Paiement & inscription",
    },
    {
      text: "Après chaque versement, un reçu UPL vous est délivré : joignez-le à vos documents d'inscription.",
      source: "Justificatifs",
    },
  ],

  /* Défilement continu « À la une » : communiqués + infos pratiques. */
  tickerExtra: [
    "Cours du soir 17h–21h · Sablière, Libreville",
    "Scolarité payable en tranches · reçu + confirmation UPL",
    "Inscriptions : contact@upl-gabon.com",
  ],

  /* Citations de management — rotation aléatoire côté accueil.
     Choisir des citations sourcées (attribution fiable). */
  quotes: [
    {
      text: "Le management consiste à faire les choses correctement ; le leadership, à faire les bonnes choses.",
      author: "Peter Drucker",
    },
    {
      text: "Les plans ne sont que de bonnes intentions tant qu'ils ne se transforment pas immédiatement en travail.",
      author: "Peter Drucker",
    },
    {
      text: "La meilleure façon de prédire l'avenir, c'est de le créer.",
      author: "Peter Drucker",
    },
    {
      text: "Quiconque cesse d'apprendre vieillit — qu'il ait vingt ou quatre-vingts ans.",
      author: "Henry Ford",
    },
    {
      text: "L'éducation est l'arme la plus puissante qu'on puisse utiliser pour changer le monde.",
      author: "Nelson Mandela",
    },
    {
      text: "Un budget, c'est dire à son argent où aller, au lieu de se demander où il est passé.",
      author: "John C. Maxwell",
    },
  ],

  /* Communiqués / actualités de l'école — mis à jour ICI (le plus récent en premier).
     Utiliser des faits réels ; date au mois, pas de date inventée. */
  news: [
    {
      tag: "Communiqué",
      date: "Août 2026",
      title: "Inscriptions ouvertes — Executive MBA",
      text: "Constitution du dossier : CV, parcours, diplômes — par e-mail (objet « Candidature MBA ») ou dépôt au secrétariat, Sablière. Scolarité payable en tranches.",
    },
    {
      tag: "Vie de l'école",
      date: "",
      title: "Les cours du soir se poursuivent à la Sablière",
      text: "Séances de 17h00 à 21h00, compatibles avec l'activité professionnelle des auditeurs. Emploi du temps remis au début de chaque module.",
    },
    {
      tag: "Inscription",
      date: "",
      title: "Paiement : justificatif et confirmation UPL indispensables",
      text: "Règlement des tranches par Airtel Money ou au secrétariat. Conservez votre justificatif de paiement : la confirmation de l'UPL complète votre dossier d'inscription.",
    },
    {
      tag: "Multimédia",
      date: "",
      title: "L'UPL en vidéo",
      text: "Présentation institutionnelle à la télévision (lecture automatique sur l'accueil) et interview sur l'Executive MBA — page MBA, section « Le MBA en images ».",
    },
  ],

  deploy: {
    domain: "upl-gabon.com",
    emailProvider: "PrivateEmail / Namecheap",
    preferredHost: "GitHub Pages",
    keepNetlifyUntilFinal: true,
  },
};
