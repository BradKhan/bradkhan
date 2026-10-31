# Contributing compositions

A valuable contribution is not another link. It's a useful *combination* of existing capabilities.

## Propose an entry

Open a GitHub issue in the profile repository identifying:
1. A specific human problem and who experiences it.
2. At least two source projects with their canonical links and licenses.
3. Exactly what the existing projects already do.
4. The smallest original adapter, interface or workflow needed.
5. A demonstrable outcome that could be independently tested.
6. Platform restrictions, privacy issues, operating costs and unknowns.

A good entry might save someone a tedious recurring step, restore portability, improve independent verification, or make a sophisticated tool available to people who don't write code.

## Implementation evidence

Change the status from `concept_not_integrated` only when code and reproducible evidence are published. Report both passing and failing cases. Actual media, images and user data must be used with appropriate permission.

## Maintenance

Edit `data/compositions.json` and the matching section in `README.md`, then run:

```bash
python3 composable-internet/scripts/validate.py
```

This validates structure and cross references, not the live availability, security or licensing of upstream repositories. Those must still be reviewed by a person.

This collection is currently located in the profile repository. A standalone repository can adopt its files unchanged.
