Reference
=========
.. py:currentmodule:: tp24

Models
------

.. py:class:: Colour

   The parent class of all colour classes.

   .. versionadded:: 1.0

   .. warning::
      Do not use Colour itself to specify a colour.
      Use classes inherited from :py:class:`Colour`, eg :py:class:`rgb`, :py:class:`cmyk`, etc.

   .. description:: Operations

      * **a+b** - adds each channel together to lighten the colour.
      * **a-b** - subtracts channel in b from channel in a to darken the colour.
      * **a*b** - Calls :py:func:``tools.gradient``(a, b) with equal proportion to mix the colours.
      * **x for x in a** - Gets the value of each channel of the colour.

      When adding colours of different models, the second colour will be converted into the first colour's model and the result will be in the first colour's model.

   .. py:method:: hexv(compress: bool=False)

      Get the hexadecimal code of the colour.

      .. versionadded:: 1.0

      :param bool compress: Whether to give a short code if possible
      :return: The hex code
      :rtype: str

   .. py:classmethod:: from_hex(hexc: str)

      Loads a colour from a hexadecimal code.

      .. versionadded:: 1.0

      .. code-block:: python
         >>> tp24.rgb.from_hex("#f00")
         rgb(255, 0, 0)

      :param str hexc: The hex code
      :return: A colour
      :rtype: Colour
      :raises ValueError: if the hex code is invalid

   .. py:classmethod:: from_web(web: str)
       
      Loads a colour from a HTML colour name. Currently, there are 140 of them.

      .. versionadded:: 1.0

      .. code-block:: python
         >>> tp24.rgb.from_web("red")
         rgb(255, 0, 0)

      :param str web: The name of the colour
      :return: A colour
      :rtype: Colour
      :raises ValueError: if the name is invalid

   .. py:method:: inverted()

      Inverts all the channel values in the colour and returns the result.

      The original colour is unchanged.

      .. versionadded:: 1.0

      :return: The inverted colour.
      :rtype: Colour

   .. py:method:: wheel(colours: int, degree: int=None)

      Gets colours on the colour wheel.

      .. versionadded:: 1.0

      :param str colours: The number of colours to get from the wheel.
      :param int or None degree: The interval between colours in degrees.
      :return: The colours
      :rtype: tuple[Colour]
      :raises RangeError: if ``degree`` < 0 or ``degree`` > 180
      :raises RangeError: if ``colour`` ≤ 0

   .. py:method:: complementary()

      Gets the complementary colour.

      .. versionadded:: 1.0
      
      Alias of ``wheel(1)[0]``, and

      :rtype: Colour

   .. py:method:: triadic()

      Gets the two other colours in the traidic set of colours.

      .. versionadded:: 1.0
   
      Alias of ``wheel(2)``

   .. py:method:: tetradic()

      Gets the three other colours in the tetradic set of colours.

      .. versionadded:: 1.0
   
      Alias of ``wheel(3)``

   .. py:method:: analogous(degree: int=30)

      Gets the two anaologous colours.

      .. versionadded:: 1.0

      Alias of ``wheel(2, degree)``

   .. py:method:: compound(degree: int=30)

      Gets the two compound colours (analogous colours of the complementary colour).

      .. versionadded:: 1.0

      Alias of ``complementary().analogous(degree)``

   .. py:method:: add_alpha(va: int)

      Adds an alpha channel to the colour and returns the result.

      The original colour is unchanged.

      .. versionadded:: 1.0

      :param int va: the value for the alpha channel
      :return: The colour with an alpha channel.
      :rtype: Colour

.. py:class:: ColourAlpha

   A class that is a supplement to :py:class:`Colour` which adds transparency.

   .. versionadded:: 1.0

   .. warning::
      Do not use ColourAlpha itself to specify a colour.
      In fact this class is not inherited from :py:class:`Colour`
      Use classes inherited from :py:class:`Colour`, eg :py:class:`rgba`, :py:class:`cmyka`, etc.

   .. method:: __init__(va: int)

      Instantiating a colour with an alpha channel requires an additional parameter after all the other parameters.

      .. versionadded:: 1.0

      :param int va: the value for the alpha channel
      :raises RangeError: if ``alpha`` < 0 or ``alpha`` > 100

   .. py:method:: remove_alpha()

      Removes the alpha channel from the colour and returns the result.

      The original colour is unchanged.

      .. versionadded:: 1.0

      :return: The colour without an alpha channel.
      :rtype: Colour

.. py:class:: rgb(Colour)
              cmyk(Colour)
              cmy(Colour)
              hsl(Colour)
              hsv(Colour)

   A colour object.

   .. method:: __init__(...)

      Instantiating a colour requires the values of each channel of the colour.

      .. versionadded:: 1.0

      **RGB**

      :param int vr: The value of the red channel *(0 ≤ r ≤ 255)*
      :param int vg: The value of the green channel *(0 ≤ g ≤ 255)*
      :param int vb: The value of the blue channel *(0 ≤ b ≤ 255)*

      **CMY(K)**

      :param int vc: The value of the cyan channel *(0 ≤ c ≤255)*
      :param int vm: The value of the magenta channel *(0 ≤ m ≤ 255)*
      :param int vy: The value of the yellow channel *(0 ≤ y ≤ 255)*
      :param int vk: The value of the key (CMYK only) *(0 ≤ k ≤ 255)*

      **HSL/V**

      :param int vh: The hue *(0 ≤ h ≤ 360)*
      :param int vs: The saturation *(0 ≤ s ≤ 100)
      :param int vl: The lightness (HSL only) *(0 ≤ l ≤ 100)*
      :param int vv: The value (HSV only) *(0 ≤ v ≤ 100)*

   .. method:: rgb()
               cmyk()
               cmy()
               hsl()
               hsv()

      Converts a colour into a colour of another model.

      The original colour is unchanged.

      Each class does not have the converting method of the same name, eg there is no ``rgb.rgb()`` but a ``cmyk.rgb()``

      .. versionadded:: 1.0

      :return: The colour in the new model.
      :rtype: Colour

   .. py:property:: RANGE
   :type: tuple[int]
      
      The maximum value of each of the channels.

      .. versionadded:: 1.0

   .. py:attribute:: r
                     g
                     b
                     c
                     m
                     y
                     k
                     h
                     s
                     l
                     v
   :type: int 

      The value of a specific channel.

      .. versionadded:: 1.0

.. py:class:: rgba(Colour, ColourAlpha)
              cmyka(Colour, ColourAlpha)
              cmya(Colour, ColourAlpha)
              hsla(Colour, ColourAlpha)
              hsva(Colour, ColourAlpha)

   A colour object, with an alpha channel.

   .. method:: __init__(..., va: int)

      Calls both __init__ functions from Colour and ColourAlpha.

      The last parameter is used as the alpha, while the other parameters define the values of the other channels.
      
      .. versionadded:: 1.0

   .. py:attribute:: a
   :type: int

      The value of the alpha channel.

      .. versionadded:: 1.0

.. py:currentmodule:: tp24.tools

Tools
-----

.. py:function:: gradient(a: Colour, b: Colour, ap: Union[int, float]=0.5, bp: Union[int, float]=0.5)

   Get a colour along a gradient between two colours. Works best in RGB.

   .. versionadded:: 1.0

   :param Colour a: The first colour
   :param Colour b: The second colour
   :param ap: The proportion of the first colour to mix
   :param bp: The proportion of the second colour to mix
   :type ap: int or float
   :type bp: int or float
   :return: The colour
   :rtype: Colour
   
.. py:function:: similarity(a: Colour, b: Colour)

   Finds the similarity of two colours by comparing the values of each channel. Works best in HSL/V.

   .. versionadded:: 1.0

   :param Colour a: The first colour
   :param Colour b: The second colour
   :return: The colour
   :rtype: Colour

.. py:currentmodule:: tp24.errors

Errors
------

.. py:exception:: RangeError

   Raised when the value provided is outside the range allowed.

   .. versionadded:: 1.0