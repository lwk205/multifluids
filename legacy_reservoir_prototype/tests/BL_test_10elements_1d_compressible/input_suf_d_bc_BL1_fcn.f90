
program input_suf_d_bc
  implicit none
  integer, parameter :: stotel = 2, cv_snloc = 1, nphase = 2
  real, dimension( stotel * cv_snloc * nphase ) :: field
  integer :: i
  real :: value

  field = 0.
  field( 1 ) = 1.

  do i = 1, stotel * nphase
    print*, field( i )
  end do

end program input_suf_d_bc