from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Could have also used CharField(read_only=True)
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('id', 'owner', 'title', 'highlight', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')


class SearchSerializer(serializers.Serializer):
    time_frame_choices = [('current', 'Current'), ('past-week', 'Past Week'), ('past-month', 'Past Month')]
    time_frame = serializers.ChoiceField(time_frame_choices)

    vulnerability_choices = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ]
    vulnerability = serializers.MultipleChoiceField(vulnerability_choices)

    # @kamquestion: what's this help_text mean?
    display_only_recent_increases = serializers.BooleanField()

    length_of_stay_choices = [('all', 'All'), ]
    length_of_stay = serializers.ChoiceField(length_of_stay_choices)

    advance_directives_choices = [('all', 'All'), ]
    advance_directives = serializers.ChoiceField(advance_directives_choices)

    discharged_to_choices = [('hospital', 'Hospital'), ('nursing-home', 'Nursing Home')]
    discharged_to = serializers.MultipleChoiceField(discharged_to_choices)

    admission_diagnoses_choices = [('none', 'None'), ]
    admission_diagnoses = serializers.ChoiceField(admission_diagnoses_choices)

    outcomes_choices = [('bad-vision', 'Bad Vision'), ('delirium', 'Delirium'), ]
    outcomes = serializers.MultipleChoiceField(outcomes_choices)

    # @kamquestion: what's this help_text mean?
    all_recent_outcomes = serializers.BooleanField()
