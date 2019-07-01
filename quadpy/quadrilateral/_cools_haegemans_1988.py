from ..helpers import article
from ._helpers import QuadrilateralScheme, concat, s4, zero

citation = article(
    authors=["R. Cools", "Ann Haegemans"],
    title="Another Step Forward in Searching for Cubature Formulae with a Minimal Number of Knots for the Square",
    journal="Computing",
    volume="40",
    pages="139-146",
    year="1988",
    url="https://doi.org/10.1007/BF02247942",
)


def cools_haegemans_1988_1():
    weights, points = s4(
        [
            0.0480207633507238145627631759775806,
            0.982639223540855472952491497004009,
            0.698076104549567564776469806174958,
        ],
        [
            0.0660713291645505956736350808495464,
            0.825775835902963937302274585289940,
            0.939486382816736907206432362169896,
        ],
        [
            0.0973867773586681641961204397995472,
            0.188586138718641954600324568182745,
            0.953539528201532015845004266823976,
        ],
        [
            0.211736349998948600503931661356261,
            0.812520548304813100489382581912299,
            0.315623432915254195985609716402104,
        ],
        [
            0.225626061728863387403158016208490,
            0.525320250364547762341631887140024,
            0.712001913075336306549065895123759,
        ],
        [
            0.351158718398245437660391625808574,
            0.0416580719120223682735468045377018,
            0.424847248848669250615430111511957,
        ],
    )
    return QuadrilateralScheme("Cools-Haegemans 1988-1", weights, points, 11, citation)


def cools_haegemans_1988_2():
    weights, points = concat(
        s4(
            [
                0.29991838864499131666e-01,
                0.77880971155441942252e00,
                0.98348668243987226379e00,
            ],
            [
                0.38174421317083669640e-01,
                0.95729769978630736566e00,
                0.85955600564163892859e00,
            ],
            [
                0.60424923817749980681e-01,
                0.13818345986246535375e00,
                0.95892517028753485754e00,
            ],
            [
                0.77492738533105339358e-01,
                0.94132722587292523695e00,
                0.39073621612946100068e00,
            ],
            [
                0.11884466730059560108e00,
                0.47580862521827590507e00,
                0.85007667369974857597e00,
            ],
            [
                0.12976355037000271129e00,
                0.75580535657208143627e00,
                0.64782163718701073204e00,
            ],
            [
                0.21334158145718938943e00,
                0.69625007849174941396e00,
                0.70741508996444936217e-01,
            ],
            [
                0.25687074948196783651e00,
                0.34271655604040678941e00,
                0.40930456169403884330e00,
            ],
        ),
        zero(0.30038211543122536139e00),
    )
    return QuadrilateralScheme("Cools-Haegemans 1988-2", weights, points, 13, citation)
