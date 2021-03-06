#ifndef __IS_INFORMED_PREDICATE_H__886B4621_D084_4CA4_B800_69AD4C7CD215
#define __IS_INFORMED_PREDICATE_H__886B4621_D084_4CA4_B800_69AD4C7CD215

namespace hpgl
{
	template<typename prop_t>
	class is_informed_predicate_t
	{
		const prop_t & m_prop;
	public:
		is_informed_predicate_t(const prop_t & prop): m_prop(prop)
		{}

		bool operator()(node_index_t neighbour)const
		{
			return m_prop.is_informed(neighbour);
		}
	};
}

#endif //__IS_INFORMED_PREDICATE_H__886B4621_D084_4CA4_B800_69AD4C7CD215