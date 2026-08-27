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
    tagline: "Formez-vous aujourd'hui aux métiers de demain",
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
      title: "Rentrée 2024",
      url: "https://youtu.be/SyUXYUPj6hc",
      thumb: "https://i.ytimg.com/vi/SyUXYUPj6hc/hqdefault.jpg",
      source: "U.P.L",
    },
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

  deploy: {
    domain: "upl-gabon.com",
    emailProvider: "PrivateEmail / Namecheap",
    preferredHost: "Netlify",
    keepNetlifyUntilFinal: true,
  },
};
