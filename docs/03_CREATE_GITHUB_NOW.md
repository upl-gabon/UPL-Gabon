# Créer GitHub UPL en 10 minutes

**Email du compte :** `contact@upl-gabon.com`  
**But :** repo privé pour reprise IA ou humaine, propriété institutionnelle.

## Checklist

1. [ ] PrivateEmail ouvert — vous recevez les mails `contact@`
2. [ ] https://github.com/signup → email `contact@upl-gabon.com`
3. [ ] Username : `upl-gabon` (ou autre libre)
4. [ ] Mot de passe fort → sauvé coffre UPL (Président + Calvin)
5. [ ] Confirmer email (boîte PrivateEmail)
6. [ ] Settings → Password and authentication → **2FA TOTP** (Authy / Google Authenticator / Aegis)
7. [ ] (Rec.) Organizations → New : `upl-gabon`
8. [ ] New repository **Private** : `site-web`
9. [ ] Description : `Site institutionnel UPL — MBA · Libreville`
10. [ ] Ne pas cocher README si le code local existe déjà
11. [ ] Invite collaborator Admin : compte GitHub de Calvin (blanchardminang00)
12. [ ] En local dans `upl-web` :

```bash
git remote remove origin 2>/dev/null
git remote add origin https://github.com/upl-gabon/site-web.git
git branch -M main
git push -u origin main
```

(ou SSH si clé configurée)

13. [ ] Netlify → Add site → Import from Git → ce repo  
14. [ ] Garder l’ancien site Netlify jusqu’à validation finale  
15. [ ] `npm test` vert avant chaque mise en prod  

## Si bloqué

- GitHub ne valide pas contact@ → Plan B org + compte Gmail (voir HANDOVER.md §3)  
- Pas d’accès SSH → HTTPS + Personal Access Token (scope `repo`)  
- Token : GitHub → Settings → Developer settings → PAT — **ne jamais committer le token**
