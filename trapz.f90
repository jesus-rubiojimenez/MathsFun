module numint

    ! Numerical integration
    ! Adapted from: https://pranabdas.github.io/fortran/integration
    !
    ! Created: June 2023
    ! Modified: --

    use, intrinsic :: iso_fortran_env
    implicit none
    private
    public :: trapz

    contains

        function trapz(f, a, b, n) result(integral_result)

            interface
                function f(x) result(f_result)

                    use, intrinsic :: iso_fortran_env
                    real(real64), intent(in) :: x
                    real(real64) :: f_result
                    
                end function f
            end interface

            real(real64), intent(in) :: a, b
            integer, intent(in) :: n
            real(real64) :: integral_result, h, area
            integer :: i

            h = (b - a) / n

            area = 0.5 * (f(a) + f(b))

            do i = 1, n-1
                area = area + f(a + i*h)
            end do

            integral_result = h * area
        
        end function trapz

end module numint