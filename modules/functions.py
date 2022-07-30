class financialNoGAAP:

    def margin_EBITDA(tck):
        '''
        Use: Comparar la rentabilidad relativa de dos o más empresas 
        de diferentes tamaños en la misma industria.
        Reference: https://www.investopedia.com/terms/e/ebitda-margin.asp#citation-3
        '''
        return tck.info.get('ebitdaMargins')

    def margin_net(tck):
        '''
        Precaution: Como los márgenes de beneficio típicos varían 
        según el sector industrial, se debe tener cuidado al comparar 
        las cifras de diferentes negocios.
        Recomendation: Busca beneficios netos que crezcan constantemente
        sin volatilidad, mayor al 16%
        Reference: https://www.investopedia.com/terms/p/profitmargin.asp
        '''
        return tck.info.get('profitMargins')
    
    def margin_gross(tck):
        '''
        Use: Para filtrar compañias de gran calidad y ventaja competitiva duradera
        Precaution: Mantenerse alejado de compañias con margen menor al 20%
        Recomendation: use un margen mayor al 30% o 40%
        '''
        return tck.info.get('grossMargins')

    def margin_operatingExpenses1(tck):
        '''
        Precaution: Varían con la naturaleza del negocio, evitar grandes variaciones 
        Recomendation: Que sean bajos y constantes
        '''
        return tck.info.get('grossMargins')-tck.info.get('operatingMargins')

    def total_revenue(tck):
        return tck.info['totalRevenue']

    def gross_profit(tck):
        return tck.info.get('grossProfits')


    ''''
    gastos financieros menor al 15%, deuda,interes alto    
        '''