import numpy
import quadpy


def test_circle():
    scheme = quadpy.circle.krylov(3)
    scheme.integrate(
        lambda x: numpy.exp(x[0]), numpy.array([0.0, 0.3]), 0.7
    )
    scheme = quadpy.circle.krylov(5)
    scheme.integrate(
        lambda x: [numpy.exp(x[0]), numpy.exp(x[0])],
        numpy.array([[1.0, 1.0], [0.0, 0.3], [2.0, 2.0]]),
        [1.0, 0.7, 0.333],
    )
    return


def test_disk():
    scheme = quadpy.disk.peirce_1957(5)
    scheme.integrate(
        lambda x: numpy.exp(x[0]),
        numpy.array([0.0, 0.3]),
        0.7,
    )
    scheme = quadpy.disk.peirce_1957(5)
    scheme.integrate(
        lambda x: [numpy.exp(x[0]), numpy.exp(x[1])],
        numpy.array([[1.0, 1.0], [0.0, 0.3], [2.0, 2.0]]),
        [1.0, 0.7, 0.333],
    )
    return


def test_hexahedron():
    val = quadpy.hexahedron.integrate(
        lambda x: numpy.exp(x[0]),
        quadpy.hexahedron.cube_points([0.0, 1.0], [0.0, 1.0], [0.0, 1.0]),
        quadpy.hexahedron.Product(quadpy.line_segment.NewtonCotesClosed(3)),
    )

    val = quadpy.hexahedron.integrate(
        lambda x: [numpy.exp(x[0]), numpy.exp(x[1])],
        numpy.stack(
            [
                quadpy.hexahedron.cube_points([0, 1], [0, 1], [0, 1]),
                quadpy.hexahedron.cube_points([0, 1], [0, 1], [0, 1]),
                quadpy.hexahedron.cube_points([0, 1], [0, 1], [0, 1]),
                quadpy.hexahedron.cube_points([0, 1], [0, 1], [0, 1]),
                quadpy.hexahedron.cube_points([0, 1], [0, 1], [0, 1]),
            ],
            axis=-2,
        ),
        quadpy.hexahedron.Product(quadpy.line_segment.NewtonCotesClosed(3)),
    )
    assert val.shape == (2, 5)
    return


def test_line_segment():
    quadpy.line_segment.integrate(
        numpy.exp, [0.0, 1.0], quadpy.line_segment.NewtonCotesClosed(4)
    )
    quadpy.line_segment.integrate(
        numpy.exp, numpy.array([[0.0], [1.0]]), quadpy.line_segment.NewtonCotesClosed(4)
    )
    quadpy.line_segment.integrate(
        lambda x: [numpy.exp(x), numpy.sin(x), numpy.cos(x)],
        numpy.array([[0.0, 1.0], [1.0, 2.0]]),
        quadpy.line_segment.NewtonCotesClosed(4),
    )
    return


def test_pyramid():
    quadpy.pyramid.integrate(
        lambda x: numpy.exp(x[0]),
        numpy.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1]]),
        quadpy.pyramid.Felippa(3),
    )

    quadpy.pyramid.integrate(
        lambda x: [numpy.exp(x[0]), numpy.exp(x[1])],
        numpy.array(
            [
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]],
                [[1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0]],
                [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
                [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
            ]
        ),
        quadpy.pyramid.Felippa(5),
    )
    return


def test_quadrilateral():
    quadpy.quadrilateral.integrate(
        lambda x: numpy.exp(x[0]),
        quadpy.quadrilateral.rectangle_points([0.0, 1.0], [0.0, 1.0]),
        quadpy.quadrilateral.Stroud["C2 5-4"](),
    )

    val = quadpy.quadrilateral.integrate(
        lambda x: [numpy.exp(x[0]), numpy.exp(x[1])],
        numpy.stack(
            [
                quadpy.quadrilateral.rectangle_points([0.0, 1.0], [0.0, 1.0]),
                quadpy.quadrilateral.rectangle_points([0.0, 1.0], [0.0, 1.0]),
                quadpy.quadrilateral.rectangle_points([0.0, 1.0], [0.0, 1.0]),
                quadpy.quadrilateral.rectangle_points([0.0, 1.0], [0.0, 1.0]),
                quadpy.quadrilateral.rectangle_points([0.0, 1.0], [0.0, 1.0]),
            ],
            axis=-2,
        ),
        quadpy.quadrilateral.Stroud["C2 3-1"](),
    )
    assert val.shape == (2, 5)
    return


def test_e2r2():
    scheme = quadpy.e2r2.rabinowitz_richter_3()
    scheme.integrate(lambda x: numpy.exp(x[0]))
    return


def test_e2r():
    scheme = quadpy.e2r.rabinowitz_richter_5()
    scheme.integrate(lambda x: numpy.exp(x[0]))
    return


def test_sphere():
    quadpy.sphere.integrate(
        lambda x: numpy.exp(1j * x[0]) + 1j * x[0] ** 2,
        numpy.array([0.0, 0.3, 0.0]),
        0.7,
        quadpy.sphere.Lebedev("3a"),
    )

    quadpy.sphere.integrate(
        lambda x: [numpy.exp(x[0]), numpy.exp(x[1])],
        numpy.array([[1.0, 1.0, 0.0], [0.0, 0.3, 0.0], [2.0, 2.0, 0.0]]),
        [1.0, 0.7, 0.333],
        quadpy.sphere.Lebedev("3a"),
    )
    return


def test_ball():
    scheme = quadpy.ball.hammer_stroud_15_3a()
    scheme.integrate(lambda x: numpy.exp(x[0]), [0.0, 0.0, 0.0], 1.0)

    scheme = quadpy.ball.hammer_stroud_15_3b()
    scheme.integrate(
        lambda x: [numpy.exp(x[0]), numpy.exp(x[1])],
        [[1.0, 1.0, 0.0], [0.0, 0.3, 0.0], [2.0, 2.0, 0.0]],
        [1.0, 0.7, 0.333],
    )
    return


def test_tetrahedron():
    quadpy.tetrahedron.integrate(
        lambda x: numpy.exp(x[0]),
        numpy.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float),
        quadpy.tetrahedron.ShunnHam(3),
    )

    quadpy.tetrahedron.integrate(
        lambda x: [numpy.exp(x[0]), numpy.exp(x[1])],
        numpy.stack(
            [
                [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0], [0.0, 0, 1]],
                [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0], [0.0, 0, 1]],
                [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0], [0.0, 0, 1]],
                [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0], [0.0, 0, 1]],
            ],
            axis=-2,
        ),
        quadpy.tetrahedron.ShunnHam(3),
    )
    return


def test_triangle():
    quadpy.triangle.integrate(
        lambda x: numpy.exp(x[0]),
        numpy.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]]),
        quadpy.triangle.Cubtri(),
    )

    val = quadpy.triangle.integrate(
        lambda x: [numpy.exp(x[0]), numpy.exp(x[1])],
        numpy.stack(
            [
                [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]],
                [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]],
                [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]],
                [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]],
                [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]],
            ],
            axis=-2,
        ),
        quadpy.triangle.Cubtri(),
    )
    assert val.shape == (2, 5)
    return


def test_wedge():
    quadpy.wedge.integrate(
        lambda x: numpy.exp(x[0]),
        numpy.array(
            [[[0, 0, 0], [1, 0, 0], [0, 1, 0]], [[0, 0, 1], [1, 0, 1], [0, 1, 1]]]
        ),
        quadpy.wedge.Felippa[4](),
    )

    val = quadpy.wedge.integrate(
        lambda x: [numpy.exp(x[0]), numpy.exp(x[1])],
        numpy.stack(
            [
                [[[0, 0, 0], [1, 0, 0], [0, 1, 0]], [[0, 0, 1], [1, 0, 1], [0, 1, 1]]],
                [[[0, 0, 0], [1, 0, 0], [0, 1, 0]], [[0, 0, 1], [1, 0, 1], [0, 1, 1]]],
                [[[0, 0, 0], [1, 0, 0], [0, 1, 0]], [[0, 0, 1], [1, 0, 1], [0, 1, 1]]],
            ],
            axis=-2,
        ),
        quadpy.wedge.Felippa[4](),
    )
    assert val.shape == (2, 3)
    return


def test_nsimplex():
    dim = 4
    quadpy.nsimplex.integrate(
        lambda x: numpy.exp(x[0]),
        numpy.array(
            [
                [0.0, 0.0, 0.0, 0.0],
                [1.0, 2.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 3.0, 1.0, 0.0],
                [0.0, 0.0, 4.0, 1.0],
            ]
        ),
        quadpy.nsimplex.GrundmannMoeller(dim, 3),
    )
    return


def test_nball():
    dim = 4
    quadpy.nball.integrate(
        lambda x: numpy.exp(x[0]), numpy.zeros(4), 1.0, quadpy.nball.Dobrodeev1970(dim)
    )
    return


def test_ncube():
    dim = 4
    quadpy.ncube.integrate(
        lambda x: numpy.exp(x[0]),
        quadpy.ncube.ncube_points([0.0, 1.0], [0.1, 0.9], [-1.0, 1.0], [-1.0, -0.5]),
        quadpy.ncube.Stroud(dim, "Cn 3-3"),
    )
    return


def test_nsphere():
    dim = 4
    quadpy.nsphere.integrate(
        lambda x: numpy.exp(x[0]),
        numpy.zeros(dim),
        1.0,
        quadpy.nsphere.Dobrodeev1978(dim),
    )
    return


def test_enr2():
    dim = 4
    quadpy.enr2.integrate(lambda x: numpy.exp(x[0]), quadpy.enr2.Stroud["5-2"](dim))
    return


def test_e1r():
    scheme = quadpy.e1r.gauss_laguerre(5)
    scheme.integrate(lambda x: x[0] ** 2)
    return


def test_e3r():
    quadpy.e3r.integrate(lambda x: numpy.exp(x[0]), quadpy.e3r.StroudSecrest["IX"]())
    return


def test_e1r2():
    scheme = quadpy.e1r2.gauss_hermite(5)
    scheme.integrate(lambda x: x[0] ** 2)
    return


if __name__ == "__main__":
    test_sphere()
