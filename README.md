# IFRS 18 Presentation Pathfinder

A self-contained, browser-only scoping tool for exploring indicative IFRS 18 statement of profit or loss categories, disclosure changes, IAS 7 cash-flow implications and implementation priorities.

The profile library is Channel Islands-first: fund administrators and trust companies, alternative and real estate funds, GP/LP structures, PCCs and cell companies, plus local operating and public-interest organisations. The original manufacturer, manufacturer-financing, insurer and bank baselines remain available.

The site has no backend, cookies, analytics, external libraries or external fonts. All user inputs and calculations remain in the browser.

Users can download a local JSON working file and load it later to restore their inputs. Refreshing or closing the page does not preserve an entered scenario unless that working file has been saved.

The page includes:

- all five IFRS 18 profit-or-loss categories;
- technical-basis references for mapped lines;
- guided specified-expense, MPM and transition previews;
- suggested disclosure wording that is explicitly labelled as a drafting starting point;
- separate equity-method and fair-value associate/JV illustrations reflecting the June 2026 IAS 28 amendments; and
- a call to action for a detailed assessment where the scoping output indicates material change or unresolved judgement.

The accompanying [five-step user guide](output/pdf/ifrs18-pathfinder-user-guide.pdf) is included in the repository.

## Local preview

Open `index.html` directly, or run a small local static server:

```bash
python3 -m http.server 4173
```

Then visit `http://localhost:4173`.

## GitHub Pages deployment

1. Create a new GitHub repository, preferably named `ifrs18-presentation-pathfinder`.
2. Set the local branch to `main`, add the GitHub repository as `origin`, commit and push.
3. In GitHub, open **Settings → Pages**.
4. Under **Build and deployment**, select **GitHub Actions** as the source.
5. Open **Actions** and confirm that **Deploy static site to GitHub Pages** completes successfully.
6. The live URL will normally be:
   `https://<github-username>.github.io/ifrs18-presentation-pathfinder/`

Every later push to `main` validates and republishes the static site automatically.

Suggested commands after creating the empty GitHub repository:

```bash
git branch -M main
git add index.html .nojekyll README.md .github/workflows/pages.yml
git commit -m "Build IFRS 18 presentation pathfinder"
git remote add origin https://github.com/<github-username>/ifrs18-presentation-pathfinder.git
git push -u origin main
```

## Pre-launch checks

- Open all fourteen example profiles across the Channel Islands, local-business and IASB-style groups.
- Confirm financial-asset, other-asset and not-assessed investment-activity examples behave as intended.
- Confirm equity-accounted associate/JV results remain in investing and eligible FVTPL returns follow the selected main-business-activity assumption.
- Confirm the IAS 7 disclosure distinguishes entities with and without specified main business activities.
- Confirm the footer reports all embedded checks as passed.
- Test saving and restoring a JSON working file, plus the CSV download.
- Print or save the results view as PDF.
- Check the page at mobile and desktop widths.
- Open the five-step PDF guide from the hero.
- Confirm the Gerrit Heyneke link opens the intended LinkedIn profile.

## Scope

This is an indicative scoping and presentation aid, not a compliance engine, complete disclosure checklist or accounting opinion. Suggested wording is a drafting starting point only. The tool does not replace entity-specific technical analysis or professional advice.
